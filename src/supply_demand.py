from __future__ import annotations

import dataclasses
from copy import deepcopy
from typing import Self

import numpy as np
import pandas as pd

from src.drawing_utils import Point
from src.plotting_utils import configure_matplotlib
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
class Curve:
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

    def composite[C: SupplyCurve | DemandCurve](
        curves: list[C], mask: str | None = None, individual_quantities: bool = False
    ) -> C:
        [curve_type] = {type(c) for c in curves}
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
            [curve] = [c for c in curves if c.name == mask]
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


@dataclasses.dataclass
class SupplyCurve(Curve):
    name: str = "Supply Curve"
    integral_name: str = Labels.COST
    color: str = Colors.SUPPLY


@dataclasses.dataclass
class DemandCurve(Curve):
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

    def curve(self, name: str) -> Curve:
        [curve] = [c for c in self.curves if c.name == name]
        return curve

    def cost(self, mask: str | None = None) -> interp1d:
        return Curve.composite(self.supply_curves, mask).integral

    def utility(self, mask: str | None = None) -> interp1d:
        return Curve.composite(self.demand_curves, mask).integral

    def welfare(self, mask: str | None = None) -> callable[np.array, np.array]:
        return lambda quantity: self.utility(mask)(quantity) - self.cost(mask)(quantity)

    def equilibrium_quantity(self, mask: str | None = None) -> float:
        quantity_vals = np.arange(0.0, self.max_total_quantity + DX, DX).round(DECIMALS)
        welfare_vals = self.welfare()(quantity_vals)
        idxmax = np.nanargmax(welfare_vals)
        equilibrium_total_quantity = quantity_vals[idxmax]
        if mask is None:
            return equilibrium_total_quantity
        else:
            [curve_type] = {type(c) for c in self.curves if c.name == mask}
            curves = [c for c in self.curves if isinstance(c, curve_type)]
            composite_curve = Curve.composite(
                [c.upsampled for c in curves], mask, individual_quantities=True
            )
            equilibrium_individual_quantity = max(
                [
                    p.y
                    for p in composite_curve.points
                    if p.x <= equilibrium_total_quantity
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
