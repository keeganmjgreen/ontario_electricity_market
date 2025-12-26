import warnings

from matplotlib import pyplot as plt


def configure_matplotlib(fontsize: int = 12) -> None:
    warnings.filterwarnings("ignore", category=UserWarning)
    plt.rcParams.update({"text.usetex": True, "font.size": fontsize})


def rm(string: str) -> str:
    return "\n".join([rf"\rm {line}" for line in string.split("\n")])
