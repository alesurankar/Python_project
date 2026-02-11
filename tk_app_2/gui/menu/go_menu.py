import tkinter as tk


def create_go_menu(root, menubar):
    go_menu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Go", menu=go_menu)
    return go_menu