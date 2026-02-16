import tkinter as tk


class Bar(tk.Frame):
    def __init__(self, root, state, width, height, border, bg_color=None):
        super().__init__(root, width=width, height=height)
        self.state = state
        self.theme = state.theme

        # Canvas to handle flexible button placement
        self.canvas = tk.Canvas(
            self, 
            bg=bg_color, 
            highlightthickness=border, 
            width=width,
            height=height 
        )
        self.canvas.pack(fill="both", expand=True)