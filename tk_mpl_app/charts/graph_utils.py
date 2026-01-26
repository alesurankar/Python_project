from data.data import Data

def clear_graph(fig):
    """Clears the figure and returns a new Axes object."""
    fig.clear()
    return fig.add_subplot(111)

def set_labels(ax, graph_type):
    """Sets title and axis labels for the current graph."""
    ax.set_title(f"{Data.title} ({graph_type})")
    ax.set_xlabel(Data.x_label)
    ax.set_ylabel(Data.y_label)
    if graph_type in {'plot', 'bar', 'barh', 'scatter', 'fill_between', 'step', 'errorbar', 'hist', 'pie'}:
        ax.legend()