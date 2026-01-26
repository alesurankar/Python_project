import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from charts.graphs import DrawGraph
from gui.navigation import MakeNavigationButtons
from gui.menus import CreateMenus


def CreateGui(root):
    # Plot frame
    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    fig = plt.Figure(figsize=(8, 5))
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Graph logic
    GRAPH_TYPES = [
        'plot',          # line plots
        'bar',           # vertical bars
        'barh',          # horizontal bars
        'scatter',       # points
        'fill_between',  # area under curve
        'step',          # step plot
        'errorbar',      # line with error bars
        'hist',          # histogram
        'boxplot',       # box & whisker
        'violinplot',    # violin plot
        'pie',           # pie chart
        'candlestick',
    ]
    current_graph_index = 0

    def ShowGraph(graphType):
        DrawGraph(fig, graphType)
        canvas.draw()

    def ShowNext():
        nonlocal current_graph_index
        current_graph_index = (current_graph_index + 1) % len(GRAPH_TYPES)
        ShowGraph(GRAPH_TYPES[current_graph_index])

    def ShowPrev():
        nonlocal current_graph_index
        current_graph_index = (current_graph_index - 1) % len(GRAPH_TYPES)
        ShowGraph(GRAPH_TYPES[current_graph_index])

    # Menus
    CreateMenus(root, fig)
        
    # Navigation buttons
    top_frame = ttk.Frame(root, padding=5)
    top_frame.pack(side="top", fill="x")
    MakeNavigationButtons(top_frame, ShowNext, ShowPrev)

    # Initial graph
    ShowGraph('plot')

    return fig, canvas