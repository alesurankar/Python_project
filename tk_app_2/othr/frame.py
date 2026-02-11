import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, root, dim, border, bg_color=None):
        super().__init__(root)

        # Canvas to handle flexible button placement
        self.canvas = tk.Canvas(
            self, 
            bg=bg_color, 
            highlightthickness=border,
            height=dim, 
            width=dim
        )
        self.canvas.pack(fill="both", expand=True)