import tkinter as tk


def create_edit_menu(root, menubar):
    edit_menu = tk.Menu(menubar, tearoff=0)

    edit_menu.add_command(label="Undo")
    edit_menu.add_command(label="Redo")
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")
    edit_menu.add_separator()
    edit_menu.add_command(label="Find")
    edit_menu.add_command(label="Replace")
    edit_menu.add_separator()
    edit_menu.add_command(label="Find in Files")
    edit_menu.add_command(label="Replace in Files")
    edit_menu.add_separator()
    edit_menu.add_command(label="Toggle Line Comment")
    edit_menu.add_command(label="Toggle Block comment")
    edit_menu.add_command(label="Emmet: Expand Abbreviation")
    menubar.add_cascade(label="Edit", menu=edit_menu)
    return edit_menu