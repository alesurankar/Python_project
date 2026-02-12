import tkinter as tk
from gui.menu.commands import edit_cmd
from gui.menu.helper import menu_helpers as helper


def create_edit_menu(root, theme, menubar):
    edit_menu = tk.Menu(
        menubar,
        tearoff=0,
        bg=theme.get("menu_bg"),
        fg=theme.get("menu_text"),
        activebackground=theme.get("menu_bg_hover"),
        activeforeground=theme.get("menu_text_hover"),
    )

    edit_menu.add_command(label="Undo", command=helper.cmd("undo", edit_cmd))
    edit_menu.add_command(label="Redo", command=helper.cmd("redo", edit_cmd))
    edit_menu.add_separator()
    edit_menu.add_command(label="Cut", command=helper.cmd("cut", edit_cmd))
    edit_menu.add_command(label="Copy", command=helper.cmd("copy", edit_cmd))
    edit_menu.add_command(label="Paste", command=helper.cmd("paste", edit_cmd))
    edit_menu.add_separator()
    edit_menu.add_command(label="Find", command=helper.cmd("find", edit_cmd))
    edit_menu.add_command(label="Replace", command=helper.cmd("replace", edit_cmd))
    edit_menu.add_separator()
    edit_menu.add_command(label="Find in Files", command=helper.cmd("find_in_files", edit_cmd))
    edit_menu.add_command(label="Replace in Files", command=helper.cmd("replace_in_files", edit_cmd))
    edit_menu.add_separator()
    edit_menu.add_command(label="Toggle Line Comment", command=helper.cmd("toggle_line_commands", edit_cmd))
    edit_menu.add_command(label="Toggle Block comment", command=helper.cmd("toggle_block_comment", edit_cmd))
    edit_menu.add_command(label="Emmet: Expand Abbreviation", command=helper.cmd("emmet_expand_abbreviation", edit_cmd))
    menubar.add_cascade(label="Edit", menu=edit_menu)
    return edit_menu





def create_edit_menu(parent, theme):
    btn = tk.Label(
        parent,
        text="Edit",
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