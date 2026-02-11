import tkinter as tk
from othr.frame import Frame


class Layout(tk.PanedWindow):
    def __init__(self, root, state):
        super().__init__(root, orient="horizontal")
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["body_bg"])

        self.EXPANDED_WIDTH = 120
        self.COLLAPSED_WIDTH = 0
        self.last_expand_width = self.EXPANDED_WIDTH

        # Primary side bar
        self.primary_side_bar = Frame(self, 120, 0, self.theme.get("primary_side_bar_bg"))
        self.add(self.primary_side_bar)

        # Main view
        self.main_view = Frame(self, 120, 0, self.theme.get("body_bg"))
        self.add(self.main_view)

        self.after(10, self.init_layout)

    def init_layout(self):
        if self.state.show_primary_side_bar.get():
            width = self.EXPANDED_WIDTH
        else:
            width = self.COLLAPSED_WIDTH

        self.paneconfigure(self.primary_side_bar, width=width, minsize=width)
        self.sash_place(0, width, 0)

    def show_expand(self):
        if not self.state.show_primary_side_bar.get():
            self.paneconfigure(self.primary_side_bar, width=self.last_expand_width)
            self.sash_place(0, self.last_expand_width, 0)
            self.state.show_primary_side_bar.set(True)

    def hide_expand(self):
        if self.state.show_primary_side_bar.get():
            try:
                self.last_expand_width = self.sash_coord(0)[0]
            except Exception:
                self.last_expand_width = self.DEFAULT_WIDTH

            self.paneconfigure(self.primary_side_bar, minsize=0, width=0)
            self.sash_place(0, 0, 0)
            self.state.show_primary_side_bar.set(False)