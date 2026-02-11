import tkinter as tk
from othr.bar import Bar
from othr.main_view import MainView


class Layout(tk.PanedWindow):
    def __init__(self, root, state):
        super().__init__(root, orient="horizontal")
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["body_bg"])

        self.EXPANDED_WIDTH = 120
        self.COLLAPSED_WIDTH = 0
        self.last_expand_width = self.EXPANDED_WIDTH

        # Expandable toolbar
        self.tool_expand = Bar(self, self.state, 120, 0, self.theme.get("tool_expand_bg"))
        self.add(self.tool_expand)

        # Main view
        self.main_view = MainView(self, self.state)
        self.add(self.main_view)

        self.after(10, self.init_layout)

    def init_layout(self):
        if self.state.show_tool_expand.get():
            width = self.EXPANDED_WIDTH
        else:
            width = self.COLLAPSED_WIDTH

        self.paneconfigure(self.tool_expand, width=width, minsize=width)
        self.sash_place(0, width, 0)

    def show_expand(self):
        if not self.state.show_tool_expand.get():
            self.paneconfigure(self.tool_expand, width=self.last_expand_width)
            self.sash_place(0, self.last_expand_width, 0)
            self.state.show_tool_expand.set(True)

    def hide_expand(self):
        if self.state.show_tool_expand.get():
            try:
                self.last_expand_width = self.sash_coord(0)[0]
            except Exception:
                self.last_expand_width = self.DEFAULT_WIDTH

            self.paneconfigure(self.tool_expand, minsize=0, width=0)
            self.sash_place(0, 0, 0)
            self.state.show_tool_expand.set(False)