import tkinter as tk
from othr.bar import Bar


class Tools(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        
        self.tool_bar = Bar(self, self.state, 50, 0, self.theme.get("tool_bg"))
        self.tool_bar.pack(side="left", fill="y")

        # Bind key
       # root.bind_all("e", self.toggle_expand)

    # def update_visibility(self):
    #     if self.state.show_tool_expand.get():
    #         if not self.tool_expand.winfo_ismapped():
    #             self.tool_expand.pack(side="left", fill="y")
    #     else:
    #         self.tool_expand.pack_forget()

    # def toggle_expand(self, event=None):
    #     self.state.show_tool_expand.set(not self.state.show_tool_expand.get())
    #     self.update_visibility()

    