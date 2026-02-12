import tkinter as tk
from tkinter import messagebox
from gui.menu.commands import go_cmd
from gui.menu.helper import menu_helpers as helper


def create_go_menu(root, menubar):
    go_menu = tk.Menu(menubar, tearoff=0)

    go_menu.add_command(label="Back", command=helper.cmd("back", go_cmd))
    go_menu.add_command(label="Forward", command=helper.cmd("forward", go_cmd), state="disabled")
    go_menu.add_command(label="Last Edit Location", command=helper.cmd("last_edit_location", go_cmd))
    go_menu.add_separator()
    
    # Submenu for "Switch Editor"
    switch_editor_menu = tk.Menu(go_menu, tearoff=0)

    switch_editor_menu.add_command(label="Next Editor", command=helper.cmd("next_editor", go_cmd))
    switch_editor_menu.add_command(label="Previous Editor", command=helper.cmd("previous_editor", go_cmd))
    switch_editor_menu.add_separator()

    switch_editor_menu.add_command(label="Next Used Editor", command=helper.cmd("next_used_editor", go_cmd))
    switch_editor_menu.add_command(label="Previous Used Editor", command=helper.cmd("previous_used_editor", go_cmd))
    switch_editor_menu.add_separator()
    
    switch_editor_menu.add_command(label="Next Editor in Group", command=helper.cmd("next_editor_in_group", go_cmd))
    switch_editor_menu.add_command(label="Previous Editor in Group", command=helper.cmd("previous_editor_in_group", go_cmd))
    switch_editor_menu.add_separator()
    
    switch_editor_menu.add_command(label="Next Used Editor in Group", command=helper.cmd("next_used_editor_in_group", go_cmd))
    switch_editor_menu.add_command(label="Previous Used Editor in Group", command=helper.cmd("previous_used_editor_in_group", go_cmd))
    # End Submenu for "Switch Editor"

    go_menu.add_cascade(label="Switch Editor", menu=switch_editor_menu)
    
    # Submenu for "Switch Group"
    switch_group_menu = tk.Menu(go_menu, tearoff=0)

    switch_group_menu.add_command(label="Group 1", command=helper.cmd("group_1", go_cmd))
    switch_group_menu.add_command(label="Group 2", command=helper.cmd("group_2", go_cmd))
    switch_group_menu.add_command(label="Group 3", command=helper.cmd("group_3", go_cmd), state="disabled")
    switch_group_menu.add_command(label="Group 4", command=helper.cmd("group_4", go_cmd), state="disabled")
    switch_group_menu.add_command(label="Group 5", command=helper.cmd("group_5", go_cmd), state="disabled")
    switch_group_menu.add_separator()

    switch_group_menu.add_command(label="Next Group", command=helper.cmd("next_group", go_cmd), state="disabled")
    switch_group_menu.add_command(label="Previous Group", command=helper.cmd("previous_group", go_cmd), state="disabled")
    switch_group_menu.add_separator()
    
    switch_group_menu.add_command(label="Group Left", command=helper.cmd("group_left", go_cmd), state="disabled")
    switch_group_menu.add_command(label="Group Right", command=helper.cmd("group_right", go_cmd), state="disabled")
    switch_group_menu.add_command(label="Group Above", command=helper.cmd("group_above", go_cmd), state="disabled")
    switch_group_menu.add_command(label="Group Below", command=helper.cmd("group_below", go_cmd), state="disabled")

    # End Submenu for "Switch Group"

    go_menu.add_cascade(label="Switch Group", menu=switch_group_menu)
    go_menu.add_separator()

    go_menu.add_command(label="Go to File...", command=helper.cmd("go_to_file", go_cmd))
    go_menu.add_command(label="Go to Symbol in Workspace...", command=helper.cmd("go_to_symbol_in_workspace", go_cmd))
    go_menu.add_separator()
    
    go_menu.add_command(label="Go to Symbol in Editor...", command=helper.cmd("go_to_symbol_in_editor", go_cmd))
    go_menu.add_command(label="Go to Definition", command=helper.cmd("go_to_definition", go_cmd))
    go_menu.add_command(label="Go to Declaration", command=helper.cmd("go_to_declaration", go_cmd))
    go_menu.add_command(label="Go to Implementations", command=helper.cmd("go_to_implementations", go_cmd))
    go_menu.add_command(label="Go to References", command=helper.cmd("go_to_references", go_cmd))
    go_menu.add_separator()
    
    go_menu.add_command(label="Go to Line/Column", command=helper.cmd("go_to_line_and_column", go_cmd))
    go_menu.add_command(label="Go to Bracket", command=helper.cmd("go_to_bracket", go_cmd))
    go_menu.add_separator()
    
    go_menu.add_command(label="Next Problem", command=helper.cmd("next_problem", go_cmd))
    go_menu.add_command(label="Previous Problem", command=helper.cmd("previous_problem", go_cmd))
    go_menu.add_separator()

    go_menu.add_command(label="Next Change", command=helper.cmd("next_change", go_cmd))
    go_menu.add_command(label="Previous Change", command=helper.cmd("previous_change", go_cmd))

    menubar.add_cascade(label="Go", menu=go_menu)
    return go_menu
