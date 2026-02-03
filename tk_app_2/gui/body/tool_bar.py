import tkinter as tk
from othr.bar import Bar


class ToolBar(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        
        self.tool_bar = Bar(self, self.state, 50, 0, self.theme.get("tool_bg"))
        self.tool_bar.pack(side="left", fill="y")

        self._create_buttons()
    
    def _create_buttons(self):
        c = self.tool_bar.canvas   # shortcut

        # button size
        size = 36
        pad = 8

        self.btn1 = tk.Button(c, text="A")
        self.btn2 = tk.Button(c, text="B")
        self.btn3 = tk.Button(c, text="C")

        # place vertically (like VS Code)
        c.create_window(25, pad + size * 0 + pad * 0, window=self.btn1, anchor="n")
        c.create_window(25, pad + size * 1 + pad * 1, window=self.btn2, anchor="n")
        c.create_window(25, pad + size * 2 + pad * 2, window=self.btn3, anchor="n")