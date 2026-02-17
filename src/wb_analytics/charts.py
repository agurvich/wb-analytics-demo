"""Chart styling and rendering helpers."""

PALETTE = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]


def plot_yoy_change(ax, values):
    """Plot a year-over-year change series."""
    ax.plot(values)
    ax.set_ylim(min(values) - 0.01, max(values) + 0.01)
