import tkinter as tk


def create_view_menu(root, menubar):
    # View menu
    view_menu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="View", menu=view_menu)
    return view_menu