import tkinter as tk
from gui.menu.commands import selection_cmd
from gui.menu.helper import menu_helpers as helper


def create_selection_menu(root, theme, menubar):
    selection_menu = tk.Menu(
        menubar,
        tearoff=0,
        bg=theme.get("menu_bg"),
        fg=theme.get("menu_text"),
        activebackground=theme.get("menu_bg_hover"),
        activeforeground=theme.get("menu_text_hover"),
    )

    selection_menu.add_command(label="Select All", command=helper.cmd("select_all", selection_cmd))
    selection_menu.add_command(label="Expand Selection", command=helper.cmd("expand_selection", selection_cmd))
    selection_menu.add_command(label="Shrink Selection", command=helper.cmd("shrink_selection", selection_cmd))
    selection_menu.add_separator()

    selection_menu.add_command(label="Copy Line Up", command=helper.cmd("copy_line_up", selection_cmd))
    selection_menu.add_command(label="Copy Line Down", command=helper.cmd("copy_line_down", selection_cmd))
    selection_menu.add_command(label="Move Line Up", command=helper.cmd("move_line_up", selection_cmd))
    selection_menu.add_command(label="Move Line Down", command=helper.cmd("move_line_down", selection_cmd))
    selection_menu.add_command(label="Duplicate Selection", command=helper.cmd("duplicate_selection", selection_cmd))
    selection_menu.add_separator()

    selection_menu.add_command(label="Add Cursor Above", command=helper.cmd("add_cursor_above", selection_cmd))
    selection_menu.add_command(label="Add Cursor Below", command=helper.cmd("add_cursor_below", selection_cmd))
    selection_menu.add_command(label="Add Cursors to Line Ends", command=helper.cmd("add_cursor_to_line_ends", selection_cmd))
    selection_menu.add_command(label="Add Next Occurrence", command=helper.cmd("add_next_occurrence", selection_cmd))
    selection_menu.add_command(label="Add Previous Occurrence", command=helper.cmd("add_previous_occurrence", selection_cmd))
    selection_menu.add_command(label="Select All Occurrences", command=helper.cmd("select_all_occurrences", selection_cmd))
    selection_menu.add_separator()

    selection_menu.add_command(label="Switch to Ctrl+Click for Multi-Cursor", command=helper.cmd("switch_to_ctrl_and_click_for_multi_cursor", selection_cmd))
    selection_menu.add_command(label="Column Selection Mode", command=helper.cmd("column_selection_mode", selection_cmd))

    menubar.add_cascade(label="Selection", menu=selection_menu)
    return selection_menu




def create_selection_menu2(parent, theme):
    btn = tk.Label(
        parent,
        text="Selection",
        font=("Segoe UI Emoji", 10),
        bg=theme.get("menu_bar_bg"),
        fg=theme.get("menu_bar_text"),
        padx=6,
        pady=4,
    )
    btn.pack(side="left", padx=2)

    # Optional: hover effect
    def on_enter(e):
        btn.config(bg=theme.get("menu_bar_bg_hover"))

    def on_leave(e):
        btn.config(bg=theme.get("menu_bar_bg"))

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return {"button": btn}