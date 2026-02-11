import tkinter as tk
from gui.menu.all_menus import create_file_menu, create_edit_menu, create_selection_menu, create_view_menu, create_go_menu, create_run_menu, create_terminal_menu, create_help_menu


class MenuBar:
    def __init__(self, root, state):
        self.root = root
        self.state = state

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        self.file_menu = create_file_menu(self.root, menubar)
        self.edit_menu = create_edit_menu(self.root, menubar)
        self.selection_menu = create_selection_menu(self.root, menubar)
        self.view_menu = create_view_menu(self.root, menubar)
        self.go_menu = create_go_menu(self.root, menubar)
        self.run_menu = create_run_menu(self.root, menubar)
        self.terminal_menu = create_terminal_menu(self.root, menubar)
        self.help_menu = create_help_menu(self.root, menubar)


    