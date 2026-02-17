import tkinter as tk
from othr.bar import Bar
from gui.menu.file_menu import expand_file_menu
from gui.menu.edit_menu import expand_edit_menu
from gui.menu.selection_menu import expand_selection_menu
from gui.menu.view_menu import expand_view_menu, colapse_view_menu
from gui.menu.go_menu import expand_go_menu
from gui.menu.run_menu import expand_run_menu
from gui.menu.terminal_menu import expand_terminal_menu
from gui.menu.help_menu import expand_help_menu


class MenuBar(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        #self.active_menu = None
        self.buttons = {}

        self.menu_bar = Bar(self, self.state, 0, 30, 0, self.theme.get("menu_bar_bg"))
        self.menu_bar.pack(side="top", fill="x")


        self._build_ui()
        #root.bind("<Button-1>", self._close_all, add="+")


    # ---------- build UI ----------
    def _build_ui(self):
        c = self.menu_bar.canvas

        # Menu names and their expand functions
        menus = {
            "File": (expand_file_menu, None),
            "Edit": (expand_edit_menu, None),
            "Selection": (expand_selection_menu, None),
            "View": (expand_view_menu, colapse_view_menu),
            "Go": (expand_go_menu, None),
            "Run": (expand_run_menu, None),
            "Terminal": (expand_terminal_menu, None),
            "Help": (expand_help_menu, None),
        }
        top_frame = tk.Frame(c, bg=self.theme.get("menu_bar_bg"))
        c.create_window((0, 0), window=top_frame, anchor="nw")

        for name, (expand_func, collapse_func) in menus.items():
            self._add_button(name, expand_func, collapse_func, top_frame)

        top_frame.update_idletasks()
        c.config(scrollregion=c.bbox("all"))


    # ---------- add button ----------
    def _add_button(self, name, expand_func, collapse_func, parent):
        btn = tk.Label(
            parent,
            text=name,
            font=("Segoe UI Emoji", 10),
            bg=self.theme.get("menu_bar_bg"),
            fg=self.theme.get("menu_bar_text"),
            padx=4,
            pady=4,
        )
        btn.pack(side="left", padx=2)
        self.buttons[name] = btn
        btn.tooltip = name 
        btn.expand_func = expand_func
        btn.collapse_func = collapse_func
        btn._menu_open = False


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
        btn.bind("<Button-1>", lambda e: self._toggle_menu(btn, expand_func, collapse_func))
    

    # ---------- toggle menu ----------
    def _toggle_menu(self, btn, expand_func, collapse_func):
        # CLOSE if already open
        if btn._menu_open:
            collapse_func(btn)

            btn._menu_open = False
            return
        
        # OPEN menu
        expand_func(btn, self.state)
        btn._menu_open = True

        # detect outside click  
        def close_menu(event): 
            # ignore clicks on button or menu
            if event.widget is btn:
                return
            
            # close menu
            collapse_func(btn)
            # remove the binding after closing
            btn._menu_open = False
            self.unbind_all("<Button-1>")

        self.bind_all("<Button-1>", close_menu, add="+")
