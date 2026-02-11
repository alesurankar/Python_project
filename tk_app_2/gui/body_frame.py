import tkinter as tk
from gui.body.layout_frame import Layout
from gui.body.activity_bar import ActivityBar


class BodyFrame(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["body_bg"])

        self.layout = Layout(self, self.state)
        self.layout.pack(side="right", fill="both", expand=True)
        
        self.activity_bar = ActivityBar(self, self.state, layout=self.layout)
        self.activity_bar.pack(side="left", fill="y")
