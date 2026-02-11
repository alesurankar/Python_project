import tkinter as tk


def create_edit_menu(root, menubar):
    # Edit menu
    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Undo")
    edit_menu.add_command(label="Redo")
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")
    menubar.add_cascade(label="Edit", menu=edit_menu)
    return edit_menu