import dataclasses

from matplotlib.axes import Axes
import numpy as np

from src.drawing_utils import Arrow, Point
from src.plotting_utils import rm
from src.supply_demand import (
    DX,
    Curve,
    Colors,
    DemandCurve,
    SupplyCurve,
    SupplyDemand,
)


@dataclasses.dataclass
class _BasePlotter:
    ax: Axes
    xlim: tuple[float, float] = (0.0, 10.0)
    ylim: tuple[float, float] = (0.0, 10.0)
    xticks: dict[float, str] | None = None
    yticks: dict[float, str] | None = None
    xaxis_label: str = "$Q$"
    yaxis_label: str = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        self.x_vals = np.arange(self.xlim[0], self.xlim[1] + DX, DX)

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
        Arrow.vertical(y1=self.ylim[0], y2=(self.ylim[1] * 1.1)).drawn(
            self.ax
        ).end.labeled(self.ax, self.yaxis_label, va="bottom")

    def legend(self) -> None:
        self.ax.legend(loc="lower left", bbox_to_anchor=(0.95, 0.5), fontsize=10)


@dataclasses.dataclass
class SupplyDemandPlotter(_BasePlotter):
    yaxis_label: str = "$P$"

    def plot(
        self,
        curve: SupplyCurve | DemandCurve,
        equilibrium_quantity: float | None = None,
    ) -> None:
        fmt = "o-" if curve.stepped else "-"
        self.ax.plot(
            curve.xs,
            curve.ys,
            fmt,
            color=curve.color,
            drawstyle=("steps" if curve.stepped else "default"),
            label=rm(curve.name),
        )

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
                label=rm(f"{curve.integral_name}, {curve.integral_symbol}"),
            )

    def plot_all(self, supply_demand: SupplyDemand) -> None:
        equilibrium = supply_demand.equilibrium
        equilibrium_quantity = equilibrium.x if equilibrium is not None else None
        for curves in [supply_demand.supply_curves, supply_demand.demand_curves]:
            self.plot(Curve.aggregate(curves), equilibrium_quantity)
        if equilibrium is not None:
            equilibrium.drawn(self.ax)
        self.legend()


@dataclasses.dataclass
class CostUtilityPlotter(_BasePlotter):
    yaxis_label: str = r"$\mathdollar$"

    def plot_cost_or_utility_vals(
        self,
        quantity_vals: np.ndarray,
        cost_or_utility_vals: np.ndarray,
        curve_or_type: SupplyCurve | DemandCurve | type[SupplyCurve | DemandCurve],
        equilibrium_quantity: float | None = None,
        label: str | None = None,
    ) -> None:
        if equilibrium_quantity is not None:
            print(
                f"{curve_or_type.integral_name}: {cost_or_utility_vals[list(quantity_vals).index(equilibrium_quantity)]:.3f}"
            )
        if label is None:
            label = f"{curve_or_type.integral_name}, {curve_or_type.integral_symbol}"
        self.ax.plot(
            quantity_vals,
            cost_or_utility_vals,
            curve_or_type.fmt,
            color=curve_or_type.color,
            label=rm(label),
        )

    def plot_cost_or_utility(
        self,
        curve: SupplyCurve | DemandCurve,
        equilibrium_quantity: float | None = None,
    ) -> None:
        self.plot_cost_or_utility_vals(
            self.x_vals, curve.integral(self.x_vals), curve, equilibrium_quantity
        )

    def plot_welfare_vals(
        self,
        quantity_vals: np.ndarray,
        welfare_vals: np.ndarray,
        equilibrium_quantity: float | None = None,
    ) -> None:
        self.ax.plot(
            quantity_vals, welfare_vals, color=Colors.WELFARE, label=rm("Welfare, $W$")
        )
        if equilibrium_quantity is not None:
            print(
                f"W(Q_opt) = {welfare_vals[list(quantity_vals).index(equilibrium_quantity)]:.3f}"
            )
            optimum = Point(equilibrium_quantity, np.nanmax(welfare_vals))
            self.ax.plot(*optimum.xy, "ko", markersize=3, label=rm("Optimum"))
        self.legend()

    def plot_welfare(self, supply_demand: SupplyDemand) -> None:
        welfare = supply_demand.welfare()
        welfare_vals = welfare(self.x_vals)
        self.plot_welfare_vals(
            self.x_vals, welfare_vals, supply_demand.equilibrium_quantity()
        )

    def plot_multiple(
        self,
        curves: list[SupplyCurve | DemandCurve],
        total: bool = False,
        equilibrium_quantity: float | None = None,
    ) -> None:
        for curve in curves:
            self.plot_cost_or_utility(
                Curve.aggregate(curves, mask=curve.name), equilibrium_quantity
            )
        if total:
            self.plot_cost_or_utility(Curve.aggregate(curves), equilibrium_quantity)
        self.legend()

    def plot_all(
        self,
        supply_demand: SupplyDemand,
        total: bool = False,
        equilibrium_quantity: float | None = None,
    ) -> None:
        for curves in [supply_demand.supply_curves, supply_demand.demand_curves]:
            self.plot_multiple(curves, total, equilibrium_quantity)
        self.plot_welfare(supply_demand)
