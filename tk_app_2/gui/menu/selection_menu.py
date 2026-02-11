import tkinter as tk


def create_selection_menu(root, menubar):
    # Selection menu
    selection_menu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Selection", menu=selection_menu)
    return selection_menu