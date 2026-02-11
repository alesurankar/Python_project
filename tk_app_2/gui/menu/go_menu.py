import tkinter as tk
from tkinter import messagebox
from gui.menu.commands import go_menu_cmd


def cmd(name):
    return lambda: dispatch(name)

def create_go_menu(root, menubar):
    go_menu = tk.Menu(menubar, tearoff=0)

    go_menu.add_command(label="Back", command=cmd("back"))
    go_menu.add_command(label="Forward", command=cmd("forward"), state="disabled")
    go_menu.add_command(label="Last Edit Location", command=cmd("last_edit_location"))
    go_menu.add_separator()
    
    # Submenu for "Switch Editor"
    switch_editor_menu = tk.Menu(go_menu, tearoff=0)

    switch_editor_menu.add_command(label="Next Editor", command=cmd("next_editor"))
    switch_editor_menu.add_command(label="Previous Editor", command=cmd("previous_editor"))
    switch_editor_menu.add_separator()

    switch_editor_menu.add_command(label="Next Used Editor", command=cmd("next_used_editor"))
    switch_editor_menu.add_command(label="Previous Used Editor", command=cmd("previous_used_editor"))
    switch_editor_menu.add_separator()
    
    switch_editor_menu.add_command(label="Next Editor in Group", command=cmd("next_editor_in_group"))
    switch_editor_menu.add_command(label="Previous Editor in Group", command=cmd("previous_editor_in_group"))
    switch_editor_menu.add_separator()
    
    switch_editor_menu.add_command(label="Next Used Editor in Group", command=cmd("next_used_editor_in_group"))
    switch_editor_menu.add_command(label="Previous Used Editor in Group", command=cmd("previous_used_editor_in_group"))
    # End Submenu for "Switch Editor"

    go_menu.add_cascade(label="Switch Editor", menu=switch_editor_menu)
    
    # Submenu for "Switch Group"
    switch_group_menu = tk.Menu(go_menu, tearoff=0)

    switch_group_menu.add_command(label="Group 1", command=cmd("group_1"))
    switch_group_menu.add_command(label="Group 2", command=cmd("group_2"))
    switch_group_menu.add_command(label="Group 3", command=cmd("group_3"), state="disabled")
    switch_group_menu.add_command(label="Group 4", command=cmd("group_4"), state="disabled")
    switch_group_menu.add_command(label="Group 5", command=cmd("group_5"), state="disabled")
    switch_group_menu.add_separator()

    switch_group_menu.add_command(label="Next Group", command=cmd("next_group"), state="disabled")
    switch_group_menu.add_command(label="Previous Group", command=cmd("previous_group"), state="disabled")
    switch_group_menu.add_separator()
    
    switch_group_menu.add_command(label="Group Left", command=cmd("group_left"), state="disabled")
    switch_group_menu.add_command(label="Group Right", command=cmd("group_right"), state="disabled")
    switch_group_menu.add_command(label="Group Above", command=cmd("group_above"), state="disabled")
    switch_group_menu.add_command(label="Group Below", command=cmd("group_below"), state="disabled")

    # End Submenu for "Switch Group"

    go_menu.add_cascade(label="Switch Group", menu=switch_group_menu)
    go_menu.add_separator()

    go_menu.add_command(label="Go to File...", command=cmd("go_to_file"))
    go_menu.add_command(label="Go to Symbol in Workspace...", command=cmd("go_to_symbol_in_workspace"))
    go_menu.add_separator()
    
    go_menu.add_command(label="Go to Symbol in Editor...", command=cmd("go_to_symbol_in_editor"))
    go_menu.add_command(label="Go to Definition", command=cmd("go_to_definition"))
    go_menu.add_command(label="Go to Declaration", command=cmd("go_to_declaration"))
    go_menu.add_command(label="Go to Implementations", command=cmd("go_to_implementations"))
    go_menu.add_command(label="Go to References", command=cmd("go_to_references"))
    go_menu.add_separator()
    
    go_menu.add_command(label="Go to Line/Column", command=cmd("go_to_line_and_column"))
    go_menu.add_command(label="Go to Bracket", command=cmd("go_to_bracket"))
    go_menu.add_separator()
    
    go_menu.add_command(label="Next Problem", command=cmd("next_problem"))
    go_menu.add_command(label="Previous Problem", command=cmd("previous_problem"))
    go_menu.add_separator()

    go_menu.add_command(label="Next Change", command=cmd("next_change"))
    go_menu.add_command(label="Previous Change", command=cmd("previous_change"))

    menubar.add_cascade(label="Go", menu=go_menu)
    return go_menu


def dispatch(action):
    func = getattr(go_menu_cmd, action, None)

    if callable(func):
        func(action)
    else:
        messagebox.showinfo("Info", f"❌ Function '{action}' does not exist.")
        print("❌ Missing function:", action)