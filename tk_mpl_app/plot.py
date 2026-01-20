import matplotlib.pyplot as plt

# -----------------------------
# Data
# -----------------------------
title='Sunny Days per Month'
label_in = "Sunny Days"
sunny_days = [8,10,7,14,20,18,25,19,18,14,12,7]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y_in = sunny_days
x_in = months

avgGraphLabel = "Average Sunny Days"
avg_sunny_days = sum(sunny_days) / len(sunny_days)
y_avg = avg_sunny_days

# -----------------------------
# Definitions
# -----------------------------
xData=x_in
yData=y_in
graph_defaults = {
    'color': 'blue',
    'edgecolor': 'black',
    'linewidth': 2,
    'linestyle': '-',
    'marker': 'o',
    'markersize': 6,
    'markerfacecolor': 'orange',
    'markeredgecolor': 'black',
    'alpha': 0.8,
    'label': label_in,
    'width': 0.8,     
    'tick_label': x_in
}
avg = False

# -----------------------------
# Graph functions
# -----------------------------
def ClearGraph(fig):
    fig.clear()
    return fig.add_subplot(111)

def SetLabels(ax, graphType):
    ax.set_title(f"{title} ({graphType})")
    ax.set_xlabel('Month')
    ax.set_ylabel('Sunny Days')
    ax.legend()

def DrawGraph(fig, graphType='plot', **kwargs):
    """Draw a graph of type `graphType` on the given figure.

    kwargs can override defaults:
        color, edgecolor, linewidth, linestyle, marker,
        markersize, markerfacecolor, markeredgecolor, alpha,
        label, width, tick_label
    """
    ax = ClearGraph(fig)
    options = graph_defaults.copy()
    options.update(kwargs)

    if graphType == 'plot':
        ax.plot(
            xData, yData,
            color=options['color'],
            linestyle=options['linestyle'],
            linewidth=options['linewidth'],
            marker=options['marker'],
            markersize=options['markersize'],
            markerfacecolor=options['markerfacecolor'],
            markeredgecolor=options['markeredgecolor'],
            alpha=options['alpha'],
            label=options['label']
        )
    elif graphType == 'bar':
        ax.bar(
            xData, yData,
            color=options['color'],
            edgecolor=options['edgecolor'],
            linewidth=options['linewidth'],
            width=options['width'],
            alpha=options['alpha'],
            label=options['label'],
            tick_label=options['tick_label']
        )
    elif graphType == 'barh':
        ax.barh(
            y=xData, width=yData,
            color=options['color'],
            edgecolor=options['edgecolor'],
            linewidth=options['linewidth'],
            height=options['width'],
            alpha=options['alpha'],
            label=options['label'],
            tick_label=options['tick_label']
        )
    elif graphType == 'scatter':
        ax.scatter(
            xData, yData,
            color=options['color'],
            marker=options['marker'],
            s=options['markersize']**2,
            edgecolors=options['markeredgecolor'],
            alpha=options['alpha'],
            label=options['label']
        )
    # elif graphType == 'hist':
    #     ax.hist(x_data, label=graphLabel)
    # elif graphType == 'boxplot':
    #     ax.boxplot(y_data)
    # elif graphType == 'violinplot':
    #     ax.violinplot(y_data, color=graphColor, label=graphLabel)
    # elif graphType == 'pie':
    #     ax.pie(x_data, y_data)
    elif graphType == 'fill_between':
        ax.fill_between(
            xData, yData,
            color=options['color'],
            alpha=options['alpha'],
            label=options['label']
        )
    elif graphType == 'step':
        ax.step(
            xData, yData,
            color=options['color'],
            linewidth=options['linewidth'],
            label=options['label']
        )
    elif graphType == 'errorbar':
        ax.errorbar(
            xData, yData,
            yerr=None,
            fmt=options['marker'],
            color=options['color'],
            linewidth=options['linewidth'],
            markersize=options['markersize'],
            markerfacecolor=options['markerfacecolor'],
            markeredgecolor=options['markeredgecolor'],
            alpha=options['alpha'],
            label=options['label']
        )

    if avg and graphType in {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}:
        ax.axhline(y_avg, linestyle=options['linestyle'], color=options['color'], label=options['label'])
    SetLabels(ax, graphType)