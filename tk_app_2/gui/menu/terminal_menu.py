import tkinter as tk

    
def create_terminal_menu(root, menubar):
    terminal_menu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Terminal", menu=terminal_menu)
    return terminal_menu