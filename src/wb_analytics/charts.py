"""Chart styling and rendering helpers."""

PALETTE = ["#E69F00", "#56B4E9", "#009E73", "#CC79A7"]  # Okabe-Ito, colorblind-safe


def plot_yoy_change(ax, values):
    """Plot a year-over-year change series."""
    ax.plot(values)
    ax.set_ylim(min(values) - 0.01, max(values) + 0.01)
