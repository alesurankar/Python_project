# import tkinter as tk
# from othr.bar import Bar
# from othr.main_view import MainView


# class Window(tk.PanedWindow):
#     def __init__(self, root, state):
#         super().__init__(root, orient="vertical")
#         self.state = state
#         self.theme = state.theme
#         self.configure(bg=self.theme["body_bg"])

#         # Expandable toolbar
#         self.tool_expand = Bar(self, self.state, 60, 1, self.theme.get("tool_expand_bg"))
#         self.update_visibility()
        
#         self.nav_bar = Bar(self, self.state, 40, 1, self.theme.get("nav_bg"))
#         self.nav_bar.pack(side="top", fill="x")
        
#         self.info_bar = Bar(self, self.state, 10, 1, self.theme.get("body_bg"))
#         self.info_bar.pack(side="top", fill="x")
        
#         self.log_bar = Bar(self, self.state, 100, 2, self.theme.get("body_bg"))
#         self.log_bar.pack(side="bottom", fill="x")

#         self.scroll_bar = Bar(self, self.state, 10, 1)
#         self.scroll_bar.pack(side="right", fill="y")

#         #self.main_view = MainView(self, self.state)
        