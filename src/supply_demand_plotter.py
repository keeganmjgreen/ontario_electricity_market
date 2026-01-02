import dataclasses

from matplotlib.axes import Axes
import numpy as np

from src.drawing_utils import Arrow, Point
from src.plotting_utils import rm
from src.supply_demand import (
    Curve,
    Colors,
    DemandCurve,
    Labels,
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
        self.x_vals = np.linspace(*self.xlim, 501)

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
                label=rm(curve.integral_name),
            )

    def plot_all(self, supply_demand: SupplyDemand) -> None:
        equilibrium = supply_demand.equilibrium
        equilibrium_quantity = equilibrium.x if equilibrium is not None else None
        for curves in [supply_demand.supply_curves, supply_demand.demand_curves]:
            self.plot(Curve.composite(curves), equilibrium_quantity)
        if equilibrium is not None:
            equilibrium.drawn(self.ax)
        self.legend()


@dataclasses.dataclass
class CostUtilityPlotter(_BasePlotter):
    yaxis_label: str = r"$\mathdollar$"

    def plot_cost_or_utility(self, curve: SupplyCurve | DemandCurve) -> None:
        self.ax.plot(
            self.x_vals,
            curve.integral(self.x_vals),
            curve.fmt,
            color=curve.color,
            label=rm(curve.integral_name),
        )

    def plot_welfare(self, supply_demand: SupplyDemand) -> None:
        welfare_vals = supply_demand.welfare()(self.x_vals)
        self.ax.plot(
            self.x_vals, welfare_vals, color=Colors.WELFARE, label=rm(Labels.WELFARE)
        )
        if (equilibrium := supply_demand.equilibrium) is not None:
            optimum = Point(equilibrium.x, np.nanmax(welfare_vals))
            self.ax.plot(*optimum.xy, "ko", markersize=3, label=rm(Labels.OPTIMUM))
        self.legend()

    def plot_multiple(
        self, curves: list[SupplyCurve | DemandCurve], total: bool = False
    ) -> None:
        for curve in curves:
            self.plot_cost_or_utility(Curve.composite(curves, mask=curve.name))
        if total:
            self.plot_cost_or_utility(Curve.composite(curves))
        self.legend()

    def plot_all(self, supply_demand: SupplyDemand, total: bool = False) -> None:
        for curves in [supply_demand.supply_curves, supply_demand.demand_curves]:
            self.plot_multiple(curves, total)
        self.plot_welfare(supply_demand)
