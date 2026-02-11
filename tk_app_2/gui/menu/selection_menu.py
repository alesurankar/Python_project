import tkinter as tk


def create_selection_menu(root, menubar):
    selection_menu = tk.Menu(menubar, tearoff=0)

    selection_menu.add_command(label="Select All")
    selection_menu.add_command(label="Expand Selection")
    selection_menu.add_command(label="Shrink Selection")
    selection_menu.add_separator()
    selection_menu.add_command(label="Copy Line Up")
    selection_menu.add_command(label="Copy Line Down")
    selection_menu.add_command(label="Move Line Up")
    selection_menu.add_command(label="Move Line Down")
    selection_menu.add_command(label="Duplicate Selection")
    selection_menu.add_separator()
    selection_menu.add_command(label="Add Cursor Above")
    selection_menu.add_command(label="Add Cursor Below")
    selection_menu.add_command(label="Add Cursors to Line Ends")
    selection_menu.add_command(label="Add Next Occurrence")
    selection_menu.add_command(label="Add Previous Occurrence")
    selection_menu.add_command(label="Select All Occurrences")
    selection_menu.add_separator()
    selection_menu.add_command(label="Switch to Ctrl+Click for Multi-Cursor")
    selection_menu.add_command(label="Column Selection Mode")

    menubar.add_cascade(label="Selection", menu=selection_menu)
    return selection_menu