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


class MenuBar(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        
        self.menu_bar = Bar(self, self.state, 0, 30, 0, self.theme.get("menu_bar_bg"))
        self.menu_bar.pack(side="top", fill="x")

        self.buttons = {}

        self._build_ui()

    # ---------- button creator ----------

    def _create_menu_button(self, parent, text):
        btn = tk.Label(
            parent,
            text=text,
            font=("Segoe UI Emoji", 10),
            bg=self.theme.get("menu_bar_bg"),
            fg=self.theme.get("menu_bar_text"),
            padx=4,
            pady=4,
        )
        btn.pack(side="left", padx=2)

        def on_enter(e):
            btn.config(
                bg=self.theme.get("menu_bar_bg_hover"), 
                fg=self.theme.get("menu_bar_text_hover")
            )

        def on_leave(e):
            btn.config(
                bg=self.theme.get("menu_bar_bg"), 
                fg=self.theme.get("menu_bar_text")
            )

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        return btn
    
    # ---------- build UI ----------

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
            btn = self._create_menu_button(top_frame, name)
            self.buttons[name] = btn

            btn.bind(
                "<Button-1>",
                lambda e, f=expand_func, b=btn: f(b, self.state)
            )

        top_frame.update_idletasks()
        c.config(scrollregion=c.bbox("all"))
