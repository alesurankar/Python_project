import tkinter as tk


def create_go_menu(root, menubar):
    go_menu = tk.Menu(menubar, tearoff=0)

    go_menu.add_command(label="Back")
    go_menu.add_command(label="Forward", state="disabled")
    go_menu.add_command(label="Last Edit Location")
    go_menu.add_separator()
    
    # Submenu for "Switch Editor"
    switch_editor_menu = tk.Menu(go_menu, tearoff=0)

    switch_editor_menu.add_command(label="Next Editor")
    switch_editor_menu.add_command(label="Previous Editor")
    switch_editor_menu.add_separator()

    switch_editor_menu.add_command(label="Next Used Editor")
    switch_editor_menu.add_command(label="Previous Used Editor")
    switch_editor_menu.add_separator()
    
    switch_editor_menu.add_command(label="Next Editor in Group")
    switch_editor_menu.add_command(label="Previous Editor in Group")
    switch_editor_menu.add_separator()
    
    switch_editor_menu.add_command(label="Next Used Editor in Group")
    switch_editor_menu.add_command(label="Previous Used Editor in Group")
    # End Submenu for "Switch Editor"

    go_menu.add_cascade(label="Switch Editor", menu=switch_editor_menu)
    
    # Submenu for "Switch Group"
    switch_group_menu = tk.Menu(go_menu, tearoff=0)

    switch_group_menu.add_command(label="Group 1")
    switch_group_menu.add_command(label="Group 2")
    switch_group_menu.add_command(label="Group 3", state="disabled")
    switch_group_menu.add_command(label="Group 4", state="disabled")
    switch_group_menu.add_command(label="Group 5", state="disabled")
    switch_group_menu.add_separator()

    switch_group_menu.add_command(label="Next Group", state="disabled")
    switch_group_menu.add_command(label="Previous Group", state="disabled")
    switch_group_menu.add_separator()
    
    switch_group_menu.add_command(label="Group Left", state="disabled")
    switch_group_menu.add_command(label="Group Right", state="disabled")
    switch_group_menu.add_command(label="Group Above", state="disabled")
    switch_group_menu.add_command(label="Group Below", state="disabled")

    # End Submenu for "Switch Group"

    go_menu.add_cascade(label="Switch Group", menu=switch_group_menu)
    go_menu.add_separator()

    go_menu.add_command(label="Go to File...")
    go_menu.add_command(label="Go to Symbol in Workspace...")
    go_menu.add_separator()
    
    go_menu.add_command(label="Go to Symbol in Editor...")
    go_menu.add_command(label="Go to Definition")
    go_menu.add_command(label="Go to Declaration")
    go_menu.add_command(label="Go to Implementations")
    go_menu.add_command(label="Go to References")
    go_menu.add_separator()
    
    go_menu.add_command(label="Go to Line/Column")
    go_menu.add_command(label="Go to Bracket")
    go_menu.add_separator()
    
    go_menu.add_command(label="Next Problem")
    go_menu.add_command(label="Previous Problem")
    go_menu.add_separator()

    go_menu.add_command(label="Next Change")
    go_menu.add_command(label="Previous Change")

    menubar.add_cascade(label="Go", menu=go_menu)
    return go_menu