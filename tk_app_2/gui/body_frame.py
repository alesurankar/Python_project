import tkinter as tk
from gui.body.layout_frame import Layout
from gui.body.tool_bar import ToolBar


class BodyFrame(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["body_bg"])

        self.tool_bar = ToolBar(self, self.state)
        self.tool_bar.pack(side="left", fill="y")
        #self.add(self.left_side)

        self.layout = Layout(self, self.state)
        self.layout.pack(side="right", fill="both", expand=True)
        #self.add(self.right_side)
        