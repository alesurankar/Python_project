from data.data import Data

def ClearGraph(fig):
    """Clears the figure and returns a new Axes object."""
    fig.clear()
    return fig.add_subplot(111)

def SetLabels(ax, graphType):
    """Sets title and axis labels for the current graph."""
    ax.set_title(f"{Data.title} ({graphType})")
    ax.set_xlabel(Data.xLabel)
    ax.set_ylabel(Data.yLabel)
    if graphType in {'plot', 'bar', 'barh', 'scatter', 'fill_between', 'step', 'errorbar', 'hist', 'pie'}:
        ax.legend()