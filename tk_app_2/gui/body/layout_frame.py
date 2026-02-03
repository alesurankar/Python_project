import tkinter as tk
from othr.bar import Bar
from othr.main_view import MainView


class Layout(tk.PanedWindow):
    def __init__(self, root, state):
        super().__init__(root, orient="horizontal")
        self.state = state
        self.theme = state.theme
        self.configure(bg=self.theme["body_bg"])

        # Expandable toolbar
        self.tool_expand = Bar(self, self.state, 60, 0, self.theme.get("tool_expand_bg"))
        self.add(self.tool_expand, minsize=60)

        self.main_view = MainView(self, self.state)
        self.add(self.main_view)

        root.bind_all("e", self.toggle_expand)
        
    def toggle_expand(self, event=None):
        if self.state.show_tool_expand.get():
            # Collapse by setting pane width to 0
            self.paneconfigure(self.tool_expand, minsize=0)
            self.sash_place(0, 0, 0)
            self.state.show_tool_expand.set(False)
        else:
            # Expand again
            self.paneconfigure(self.tool_expand, minsize=60)
            self.sash_place(0, 60, 0)
            self.state.show_tool_expand.set(True)