from gui.menus import create_menus
from gui.navigation import make_navigation_buttons
from gui.actions import toggle_avg, next_graph, prev_graph
from gui.graph_widget import GraphWidget
from graphs.graphs import get_graph_types


class App:
    def __init__(self, root):
        self.root = root
        self.avg_button = None
        self.graph_widget = None

        self.create_gui()

    def create_gui(self):
        # Menus
        create_menus(self.root, self)

        # Navigation buttons
        button_config = [
            {"key": "prev", "text": "Previous", "side": "left", 
             "command": lambda: prev_graph(self, get_graph_types())},
            {"key": "avg", "text": "Toggle Avg", "side": "center", 
             "command": lambda: toggle_avg(self)},
            {"key": "next", "text": "Next", "side": "right", 
             "command": lambda: next_graph(self, get_graph_types())},
        ]
        self.nav = make_navigation_buttons(self.root, button_config)
        self.avg_button = self.nav["buttons"]["avg"]

        # Graph widget
        self.graph_widget = GraphWidget(self.root, self)
