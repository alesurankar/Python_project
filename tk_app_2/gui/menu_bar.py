import tkinter as tk
from othr.bar import Bar
from gui.menu.file_menu import expand_file_menu
from gui.menu.edit_menu import expand_edit_menu
from gui.menu.selection_menu import expand_selection_menu
from gui.menu.view_menu import expand_view_menu
from gui.menu.go_menu import expand_go_menu
from gui.menu.run_menu import expand_run_menu
from gui.menu.terminal_menu import expand_terminal_menu
from gui.menu.help_menu import expand_help_menu
from gui.menu.helpers.menu_factory import create_menu_button


class MenuBar(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        
        self.menu_bar = Bar(self, self.state, 0, 30, 0, self.theme.get("menu_bar_bg"))
        self.menu_bar.pack(side="top", fill="x")

        self.buttons = {}

        self._build_ui()

    def _build_ui(self):
        c = self.menu_bar.canvas

        # Menu names and their expand functions
        menus = {
            "File": expand_file_menu,
            "Edit": expand_edit_menu,
            "Selection": expand_selection_menu,
            "View": expand_view_menu,
            "Go": expand_go_menu,
            "Run": expand_run_menu,
            "Terminal": expand_terminal_menu,
            "Help": expand_help_menu,
        }
        top_frame = tk.Frame(c, bg=self.theme.get("menu_bar_bg"))
        c.create_window((0, 0), window=top_frame, anchor="nw")

        for name, expand_func in menus.items():
            btn = create_menu_button(top_frame, name, self.theme)  # creates a Label
            self.buttons[name] = btn

            # bind left-click to call the expand function
            btn.bind("<Button-1>", lambda e, f=expand_func, b=btn, s=self.state: f(b, s))

        top_frame.update_idletasks()
        c.config(scrollregion=c.bbox("all"))
        
