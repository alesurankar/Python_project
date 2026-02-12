import tkinter as tk
from gui.menu.file_menu import create_file_menu
from gui.menu.edit_menu import create_edit_menu
from gui.menu.selection_menu import create_selection_menu
from gui.menu.view_menu import create_view_menu
from gui.menu.go_menu import create_go_menu
from gui.menu.run_menu import create_run_menu
from gui.menu.terminal_menu import create_terminal_menu
from gui.menu.help_menu import create_help_menu


class MenuBar:
    def __init__(self, root, state):
        self.root = root
        self.state = state
        self.theme = state.theme

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        self.file_menu = create_file_menu(self.root, self.theme, menubar)
        self.edit_menu = create_edit_menu(self.root, self.theme, menubar)
        self.selection_menu = create_selection_menu(self.root, self.theme, menubar)
        self.view_menu = create_view_menu(self.root, self.theme, menubar)
        self.go_menu = create_go_menu(self.root, self.theme, menubar)
        self.run_menu = create_run_menu(self.root, self.theme, menubar)
        self.terminal_menu = create_terminal_menu(self.root, self.theme, menubar)
        self.help_menu = create_help_menu(self.root, self.theme, menubar)



from othr.bar import Bar
from gui.menu.edit_menu import create_edit_menu


class MenuBar2(tk.Frame):
    def __init__(self, root, state):
        super().__init__(root)
        self.state = state
        self.theme = state.theme
        
        self.menu_bar = Bar(self, self.state, 30, 0, self.theme.get("menu_bar_bg"))
        self.menu_bar.pack(side="top", fill="x")

        self._build_ui()
    

    def _build_ui(self):
        c = self.menu_bar.canvas

#       # buttons
        top_frame = tk.Frame(c, bg=self.theme.get("menu_bar_bg"))
        c.create_window((0, 0), window=top_frame, anchor="nw")
        
        create_file_menu(top_frame, self.theme)
        create_edit_menu(top_frame, self.theme)
        create_selection_menu(top_frame, self.theme)
        create_view_menu(top_frame, self.theme)
        create_go_menu(top_frame, self.theme)
        create_run_menu(top_frame, self.theme)
        create_terminal_menu(top_frame, self.theme)
        create_help_menu(top_frame, self.theme)

        top_frame.update_idletasks()
        c.config(scrollregion=c.bbox("all"))
        
