import tkinter as tk

    
def create_help_menu(root, menubar):
    # Help menu
    help_menu = tk.Menu(menubar, tearoff=0)
    help_menu.add_command(label="About")

    menubar.add_cascade(label="Help", menu=help_menu)
    return help_menu