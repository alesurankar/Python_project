import matplotlib.pyplot as plt

# -----------------------------
# Data
# -----------------------------
title='Sunny Days per Month'
label = "Sunny Days"
sunny_days = [8,10,7,14,20,18,25,19,18,14,12,7]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
y_data = sunny_days
x_data = months

avgGraphLabel = "Average Sunny Days"
avg_sunny_days = sum(sunny_days) / len(sunny_days)
y_avg = avg_sunny_days

# -----------------------------
# Definitions
# -----------------------------
graphColor='blue'
graphLinestyle='-'
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

def DrawGraph(fig, graphType='plot'):
    graphLabel=label
    ax = ClearGraph(fig)
    if graphType == 'plot':
        ax.plot(x_data, y_data, color=graphColor, label=graphLabel)
    elif graphType == 'bar':
        ax.bar(x_data, y_data, color=graphColor, label=graphLabel)
    elif graphType == 'barh':
        ax.barh(x_data, y_data, color=graphColor, label=graphLabel)
    elif graphType == 'scatter':
        ax.scatter(x_data, y_data, color=graphColor, label=graphLabel)
    # elif graphType == 'hist':
    #     ax.hist(x_data, label=graphLabel)
    # elif graphType == 'boxplot':
    #     ax.boxplot(y_data)
    # elif graphType == 'violinplot':
    #     ax.violinplot(y_data, color=graphColor, label=graphLabel)
    # elif graphType == 'pie':
    #     ax.pie(x_data, y_data)
    elif graphType == 'fill_between':
        ax.fill_between(x_data, y_data, color=graphColor, label=graphLabel)
    elif graphType == 'step':
        ax.step(x_data, y_data, color=graphColor, label=graphLabel)
    elif graphType == 'errorbar':
        ax.errorbar(x_data, y_data, yerr=None, fmt='o', color=graphColor, label=graphLabel)
        
    if avg and graphType in {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}:
        ax.axhline(y=y_avg, linestyle=graphLinestyle, color='green', label=avgGraphLabel)
    SetLabels(ax, graphType)