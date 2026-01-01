from __future__ import annotations

import dataclasses
from copy import deepcopy
from typing import Literal, Self

import numpy as np
import pandas as pd
from matplotlib.axes import Axes

from src.drawing_utils import Arrow, Point
from src.plotting_utils import configure_matplotlib, rm
from scipy.interpolate import interp1d

configure_matplotlib()

DX = 1e-3
DECIMALS = 10


class Labels:
    COST = "Cost, $C$"
    UTILITY = "Utility, $U$"
    WELFARE = "Welfare, $W$"
    OPTIMUM = "Optimum"


class Colors:
    SUPPLY = "#1565C0"
    DEMAND = "#EF6C00"
    WELFARE = "#2E7D32"


@dataclasses.dataclass
class _Curve:
    points: list[Point]
    name: str
    integral_name: str
    color: str
    fmt: str = "-"
    stepped: bool = True

    def __post_init__(self) -> None:
        self.integral_name = self.integral_name.replace("{name}", self.name)

    @property
    def xs(self) -> np.ndarray:
        return np.array([p.x for p in self.points])

    @property
    def ys(self) -> np.ndarray:
        return np.array([p.y for p in self.points])

    def to_series(self) -> pd.Series:
        return pd.Series(self.ys, index=self.xs)

    @property
    def func(self) -> interp1d:
        return interp1d(
            self.xs,
            self.ys,
            kind=("next" if self.stepped else "linear"),
            bounds_error=False,
        )

    @property
    def upsampled(self) -> Self:
        copy = deepcopy(self)
        quantity_vals = np.arange(self.xs.min(), self.xs.max() + DX, DX).round(DECIMALS)
        copy.points = [
            Point(x, y)
            for (x, y) in zip(quantity_vals, copy.func(quantity_vals), strict=True)
        ]
        return copy

    @property
    def integral(self) -> interp1d:
        upsampled = self.upsampled.to_series()
        if self.stepped:
            upsampled = upsampled.shift(-1)
        y_vals = np.array([0.0, *upsampled.iloc[:-1].cumsum().to_numpy()]) * DX
        return interp1d(upsampled.index, y_vals, bounds_error=False)


@dataclasses.dataclass
class SupplyCurve(_Curve):
    name: str = "Supply Curve"
    integral_name: str = Labels.COST
    color: str = Colors.SUPPLY


@dataclasses.dataclass
class DemandCurve(_Curve):
    name: str = "Demand Curve"
    integral_name: str = Labels.UTILITY
    color: str = Colors.DEMAND


@dataclasses.dataclass
class SupplyDemand:
    supply_curves: list[SupplyCurve]
    demand_curves: list[DemandCurve]
    equilibrium_price: float | None = None

    @property
    def curves(self) -> list[SupplyCurve | DemandCurve]:
        return self.supply_curves + self.demand_curves

    @property
    def upsampled(self) -> SupplyDemand:
        copy = deepcopy(self)
        for i, curve in enumerate(self.supply_curves):
            copy.supply_curves[i] = curve.upsampled
        for i, curve in enumerate(self.demand_curves):
            copy.demand_curves[i] = curve.upsampled
        return copy

    def composite_curve[C: SupplyCurve | DemandCurve](
        self,
        curve_type: type[C],
        mask: str | None = None,
        individual_quantities: bool = False,
    ) -> C:
        curves: list[SupplyCurve | DemandCurve] = {
            SupplyCurve: self.supply_curves,
            DemandCurve: self.demand_curves,
        }[curve_type]
        curve_dfs = []
        zero_quantity_prices = []
        for curve in curves:
            curve_df = pd.DataFrame(
                [
                    {"name": curve.name, "individual_quantity": p.x, "price": p.y}
                    for p in curve.points
                ]
            )
            curve_df["delta_quantity"] = (
                curve_df["individual_quantity"].diff().round(DECIMALS)
            )
            curve_dfs.append(curve_df.iloc[1:])
            zero_quantity_prices.append(curve_df.iloc[0]["price"])
        composite_df = pd.concat(curve_dfs)
        composite_df = composite_df.sort_values(
            by="price", ascending=(curve_type is SupplyCurve), kind="stable"
        )
        composite_df["total_quantity"] = (
            composite_df["delta_quantity"].cumsum().round(DECIMALS)
        )
        if mask is not None:
            composite_df.loc[
                composite_df["name"] != mask, ["individual_quantity", "price"]
            ] = 0.0
        points = [
            Point(
                round(row["total_quantity"], DECIMALS),
                row["individual_quantity"] if individual_quantities else row["price"],
            )
            for _, row in composite_df.iterrows()
        ]
        zero_quantity_price = {SupplyCurve: min, DemandCurve: max}[curve_type](
            zero_quantity_prices
        )
        points.insert(
            0,
            Point(0.0, (0.0 if individual_quantities else zero_quantity_price)),
        )
        if mask:
            [curve] = [c for c in self.curves if c.name == mask]
        [stepped] = {c.stepped for c in curves}
        return curve_type(
            points,
            name=(curve.name if mask else f"{curve_type.name} (Total)"),
            integral_name=(
                curve.integral_name if mask else f"Total {curve_type.integral_name}"
            ),
            color=(curve.color if mask else curve_type.color),
            fmt=(curve.fmt if mask else curve_type.fmt),
            stepped=stepped,
        )

    def cost(self, mask: str | None = None) -> interp1d:
        return self.composite_curve(SupplyCurve, mask).integral

    def utility(self, mask: str | None = None) -> interp1d:
        return self.composite_curve(DemandCurve, mask).integral

    def welfare(self, mask: str | None = None) -> callable[np.array, np.array]:
        return lambda quantity: self.utility(mask)(quantity) - self.cost(mask)(quantity)

    def equilibrium_quantity(self, mask: str | None = None) -> float:
        quantity_vals = np.arange(0.0, self.max_total_quantity + DX, DX).round(DECIMALS)
        welfare_vals = self.welfare()(quantity_vals)
        idxmax = np.nanargmax(welfare_vals)
        equilibrium_cumulative_quantity = quantity_vals[idxmax]
        if mask is None:
            return equilibrium_cumulative_quantity
        else:
            [curve_type] = {type(c) for c in self.curves if c.name == mask}
            composite_curve = self.upsampled.composite_curve(
                curve_type, mask, individual_quantities=True
            )
            equilibrium_individual_quantity = max(
                [
                    p.y
                    for p in composite_curve.points
                    if p.x <= equilibrium_cumulative_quantity
                ]
            )
            return equilibrium_individual_quantity

    @property
    def max_total_quantity(self) -> float:
        return sum([c.xs.max() for c in self.supply_curves])

    @property
    def equilibrium(self) -> Point | None:
        return (
            Point(self.equilibrium_quantity(), self.equilibrium_price)
            if self.equilibrium_price is not None
            else None
        )

    def plot(
        self,
        ax: Axes,
        xlim: tuple[float, float] = (0.0, 10.0),
        ylim: tuple[float, float] = (0.0, 10.0),
        xticks: dict[float, str] | None = None,
        yticks: dict[float, str] | None = None,
        xaxis_label: str = "$Q$",
        mode: PlotMode = "supply_and_demand",
        total: bool = False,
        legend: bool = True,
    ) -> None:
        plotter = SupplyDemandPlotter(ax, xlim, ylim, xticks, yticks, xaxis_label, mode)
        equilibrium_quantity = self.equilibrium_quantity()
        if mode == "cost_and_utility":
            for curve in self.curves:
                plotter.add(
                    self.composite_curve(type(curve), mask=curve.name),
                    equilibrium_quantity,
                )
        if mode == "supply_and_demand" or (mode == "cost_and_utility" and total):
            for curve in [
                self.composite_curve(SupplyCurve),
                self.composite_curve(DemandCurve),
            ]:
                plotter.add(curve, equilibrium_quantity)
        if mode == "supply_and_demand" and self.equilibrium is not None:
            self.equilibrium.drawn(ax)
        if self.supply_curves and self.demand_curves:
            if mode == "cost_and_utility":
                print(f"Q_opt = {equilibrium_quantity:.3f}")
                welfare_vals = self.welfare()(plotter.x_vals)
                ax.plot(
                    plotter.x_vals,
                    welfare_vals,
                    color=Colors.WELFARE,
                    label=rm(Labels.WELFARE),
                )
                optimum = Point(equilibrium_quantity, np.nanmax(welfare_vals))
                ax.plot(*optimum.xy, "ko", markersize=3, label=rm(Labels.OPTIMUM))
        if legend:
            plotter.legend()


type PlotMode = Literal["supply_and_demand", "cost_and_utility"]


@dataclasses.dataclass
class SupplyDemandPlotter:
    ax: Axes
    xlim: tuple[float, float] = (0.0, 10.0)
    ylim: tuple[float, float] = (0.0, 10.0)
    xticks: dict[float, str] | None = None
    yticks: dict[float, str] | None = None
    xaxis_label: str = "$Q$"
    mode: PlotMode = "supply_and_demand"

    x_vals: np.ndarray = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        self.x_vals = np.linspace(*self.xlim, 501)

        # if self.mode == "supply_and_demand":
        #     self.ax.set_aspect("equal")
        self.ax.spines[:].set_visible(False)
        self.ax.set_xlim(self.xlim[0] - 0.3, self.xlim[1] * 1.1)
        self.ax.set_ylim(self.ylim[0] - 0.3, self.ylim[1] * 1.1)
        if self.xticks is not None:
            self.ax.set_xticks(list(self.xticks.keys()))
        if self.yticks is not None:
            self.ax.set_yticks(list(self.yticks.keys()))
        if self.xticks is not None:
            self.ax.set_xticklabels(list(self.xticks.values()))
        if self.yticks is not None:
            self.ax.set_yticklabels(list(self.yticks.values()))
        Arrow.horizontal(x1=self.xlim[0], x2=(self.xlim[1] * 1.1)).drawn(
            self.ax
        ).end.labeled(self.ax, self.xaxis_label, ha="left", va="center")
        yaxis_label = {
            "supply_and_demand": "$P$",
            "cost_and_utility": r"$\mathdollar$",
        }[self.mode]
        Arrow.vertical(y1=self.ylim[0], y2=(self.ylim[1] * 1.1)).drawn(
            self.ax
        ).end.labeled(self.ax, yaxis_label, va="bottom")

    def add(self, curve: _Curve, equilibrium_quantity: float | None = None) -> None:
        if self.mode == "supply_and_demand":
            fmt = "o-" if curve.stepped else "-"
            self.ax.plot(
                curve.xs,
                curve.ys,
                fmt,
                color=curve.color,
                drawstyle=("steps" if curve.stepped else "default"),
                label=rm(curve.name),
            )

        if self.mode == "supply_and_demand":
            if equilibrium_quantity is not None:
                self.ax.fill_between(
                    self.x_vals,
                    curve.func(self.x_vals),
                    0,
                    where=(self.x_vals <= equilibrium_quantity),
                    step=("pre" if curve.stepped else None),
                    alpha=0.2,
                    color=curve.color,
                    hatch={SupplyCurve: r"\\", DemandCurve: "//"}[type(curve)],
                    edgecolor=curve.color,
                    label=rm(curve.integral_name),
                )
        if self.mode == "cost_and_utility":
            self.ax.plot(
                self.x_vals,
                curve.integral(self.x_vals),
                curve.fmt,
                color=curve.color,
                label=rm(curve.integral_name),
            )

    def legend(self) -> None:
        self.ax.legend(loc="lower left", bbox_to_anchor=(0.95, 0.5), fontsize=10)
