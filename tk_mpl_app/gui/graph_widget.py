import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from graphs.graphs import draw_graph, get_graph_types
from data.data import Data
from gui.components.theme import THEME

GRAPH_THEME = {
    'facecolor': THEME['bg'],
    'textcolor': THEME['text'],
    'tick_color': THEME['text'],
    'legend_text': THEME['text']
}

AVG_SUPPORTED = {'plot', 'bar', 'barh', 'scatter', 'step', 'errorbar'}

class GraphWidget(tk.Frame):
    def __init__(self, parent, app, default_csv="data/candles.csv"):
        super().__init__(parent, bg=THEME["bg"])
        self.pack(fill=tk.BOTH, expand=True)

        self.app = app

        # Matplotlib figure
        self.fig = plt.Figure(figsize=(8, 5), facecolor=THEME["bg"])
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas.get_tk_widget().config(bg=THEME["bg"])

        # Graph types
        self.GRAPH_TYPES = get_graph_types()

        # Load default data
        default_meta = default_csv.replace(".csv", ".meta.json")
        self.app.data = Data(default_csv, default_meta)

        # Graph state
        self.app.current_graph_index = 0
        self.app.current_graph = self.GRAPH_TYPES[0]

        # Provide a show_graph method for menus/actions
        self.app.show_graph = self.show_graph
        self.app.update_frame = self.update_frame

        # Initial draw
        self.update_frame()

    def apply_theme(self):
        for ax in self.fig.get_axes():
            ax.set_facecolor(GRAPH_THEME['facecolor'])
            ax.title.set_color(GRAPH_THEME['textcolor'])
            ax.xaxis.label.set_color(GRAPH_THEME['textcolor'])
            ax.yaxis.label.set_color(GRAPH_THEME['textcolor'])
            ax.tick_params(colors=GRAPH_THEME['tick_color'])
            legend = ax.get_legend()
            if legend:
                for text in legend.get_texts():
                    text.set_color(GRAPH_THEME['legend_text'])

    def update_frame(self):
        index = self.app.current_graph_index
        self.show_graph(self.GRAPH_TYPES[index])
        self.update_ui()

    def show_graph(self, graph_type=None, data=None):
        graph_type = graph_type or self.app.current_graph
        data = data or self.app.data
        self.app.current_graph = graph_type

        draw_graph(self.fig, graph_type, data=data)
        self.apply_theme()
        self.canvas.draw()

    def update_ui(self):
        """Show or hide Avg button using NavigationBar API, not the button itself."""
        if not hasattr(self.app, "nav"):
            return

        if self.app.current_graph in AVG_SUPPORTED:
            self.app.nav.show_avg_button()
        else:
            self.app.nav.hide_avg_button()