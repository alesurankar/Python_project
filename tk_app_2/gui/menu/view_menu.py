import tkinter as tk


def create_view_menu(root, menubar):
    view_menu = tk.Menu(menubar, tearoff=0)

    view_menu.add_command(label="Command Palette...")
    view_menu.add_command(label="Open View...")
    view_menu.add_separator()

    # Submenu for "Appearance"
    appearance_menu = tk.Menu(view_menu, tearoff=0)

    appearance_menu.add_command(label="Full Screen")
    appearance_menu.add_command(label="Zen Mode")
    appearance_menu.add_command(label="Centered Layout")
    appearance_menu.add_separator()

    root.appearance_menu_bar = tk.BooleanVar(master=root, value=True)
    root.appearance_primary_side = tk.BooleanVar(master=root, value=True)
    root.appearance_secondary_side = tk.BooleanVar(master=root, value=False)
    root.appearance_status_bar = tk.BooleanVar(master=root, value=True)
    root.appearance_panel = tk.BooleanVar(master=root, value=True)
    appearance_menu.add_checkbutton(label="Menu Bar", variable=root.appearance_menu_bar)
    appearance_menu.add_checkbutton(label="Primary Side Bar", variable=root.appearance_primary_side)
    appearance_menu.add_checkbutton(label="Secondary Side Bar", variable=root.appearance_secondary_side)
    appearance_menu.add_checkbutton(label="Status Bar", variable=root.appearance_status_bar)
    appearance_menu.add_checkbutton(label="Panel", variable=root.appearance_panel)
    appearance_menu.add_separator()

    appearance_menu.add_command(label="Move Primary Side Bar Right")

    # Submenu for "Activity Bar Position"
    activity_bar_position_menu = tk.Menu(view_menu, tearoff=0)
    root.activity_bar_position = tk.StringVar(master=root, value="Default")
    activity_bar_position_menu.add_radiobutton(label="Default", variable=root.activity_bar_position, value="Default")
    activity_bar_position_menu.add_radiobutton(label="Top", variable=root.activity_bar_position, value="Top")
    activity_bar_position_menu.add_radiobutton(label="Bottom", variable=root.activity_bar_position, value="Bottom")
    activity_bar_position_menu.add_radiobutton(label="Hidden", variable=root.activity_bar_position, value="Hidden")
    appearance_menu.add_cascade(label="Activity Bar Position", menu=activity_bar_position_menu)

    # Submenu for "Panel Position"
    panel_position_menu = tk.Menu(view_menu, tearoff=0)
    root.panel_position = tk.StringVar(master=root, value="Bottom")
    panel_position_menu.add_radiobutton(label="Top", variable=root.panel_position, value="Top")
    panel_position_menu.add_radiobutton(label="Left", variable=root.panel_position, value="Left")
    panel_position_menu.add_radiobutton(label="Right", variable=root.panel_position, value="Right")
    panel_position_menu.add_radiobutton(label="Bottom", variable=root.panel_position, value="Bottom")
    appearance_menu.add_cascade(label="Panel Position", menu=panel_position_menu)

    # Submenu for "Align Panel"
    align_panel_menu = tk.Menu(view_menu, tearoff=0)
    root.align_panel = tk.StringVar(master=root, value="Right")
    align_panel_menu.add_radiobutton(label="Center", variable=root.align_panel, value="Center")
    align_panel_menu.add_radiobutton(label="Justify", variable=root.align_panel, value="Justify")
    align_panel_menu.add_radiobutton(label="Left", variable=root.align_panel, value="Left")
    align_panel_menu.add_radiobutton(label="Right", variable=root.align_panel, value="Right")
    appearance_menu.add_cascade(label="Align Panel", menu=align_panel_menu)

    # Submenu for "Tab Bar"
    tab_bar_menu = tk.Menu(view_menu, tearoff=0)
    root.tab_bar = tk.StringVar(master=root, value="Multiple Tabs")
    tab_bar_menu.add_radiobutton(label="Multiple Tabs", variable=root.tab_bar, value="Multiple Tabs")
    tab_bar_menu.add_radiobutton(label="Single Tab", variable=root.tab_bar, value="Single Tab")
    tab_bar_menu.add_radiobutton(label="Hidden", variable=root.tab_bar, value="Hidden")
    appearance_menu.add_cascade(label="Tab Bar", menu=tab_bar_menu)

    # Submenu for "Editor Actions Position"
    editor_actions_position_menu = tk.Menu(view_menu, tearoff=0)
    root.editor_actions_position = tk.StringVar(master=root, value="Tab Bar")
    editor_actions_position_menu.add_radiobutton(label="Tab Bar", variable=root.editor_actions_position, value="Tab Bar")
    editor_actions_position_menu.add_radiobutton(label="Title Bar", variable=root.editor_actions_position, value="Title Bra")
    editor_actions_position_menu.add_radiobutton(label="Hidden", variable=root.editor_actions_position, value="Hidden")
    appearance_menu.add_cascade(label="Editor Actions Position", menu=editor_actions_position_menu)
    appearance_menu.add_separator()

    root.appearance_minimap = tk.BooleanVar(master=root, value=False)
    root.appearance_breadcrumbs = tk.BooleanVar(master=root, value=True)
    root.appearance_sticky_scroll = tk.BooleanVar(master=root, value=True)
    root.appearance_render_whitespace = tk.BooleanVar(master=root, value=True)
    root.appearance_render_control_characters = tk.BooleanVar(master=root, value=True)
    appearance_menu.add_checkbutton(label="Minimap", variable=root.appearance_minimap)
    appearance_menu.add_checkbutton(label="Breadcrumbs", variable=root.appearance_breadcrumbs)
    appearance_menu.add_checkbutton(label="Sticky Scroll", variable=root.appearance_sticky_scroll)
    appearance_menu.add_checkbutton(label="Render Whitespace", variable=root.appearance_render_whitespace)
    appearance_menu.add_checkbutton(label="Render Control Characters", variable=root.appearance_render_control_characters)
    appearance_menu.add_separator()

    appearance_menu.add_command(label="Zoom In")
    appearance_menu.add_command(label="Zoom Out")
    appearance_menu.add_command(label="Reset Zoom")
    # End Submenu for "Appearance"

    view_menu.add_cascade(label="Appearance", menu=appearance_menu)
    
    # Submenu for "Editor Layout"
    editor_layout_menu = tk.Menu(view_menu, tearoff=0)

    editor_layout_menu.add_command(label="Split Up")
    editor_layout_menu.add_command(label="Split Down")
    editor_layout_menu.add_command(label="Split Left")
    editor_layout_menu.add_command(label="Split Right")
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Split in Group")
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Move Editor into New Window")
    editor_layout_menu.add_command(label="Copy Editor into New Window")
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Single")
    editor_layout_menu.add_command(label="Two Columns")
    editor_layout_menu.add_command(label="Three Columns")
    editor_layout_menu.add_command(label="Two Rows")
    editor_layout_menu.add_command(label="Three Rows")
    editor_layout_menu.add_command(label="Grid (2x2)")
    editor_layout_menu.add_command(label="Two Rows Right")
    editor_layout_menu.add_command(label="Two Columns Bottom")
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Flip Layout")
    # End Submenu for "Editor Layout"

    view_menu.add_cascade(label="Editor Layout", menu=editor_layout_menu)
    view_menu.add_separator()

    view_menu.add_command(label="Explorer")
    view_menu.add_command(label="Search")
    view_menu.add_command(label="Source Control")
    view_menu.add_command(label="Run")
    view_menu.add_command(label="Extensions")
    view_menu.add_command(label="Testing")
    view_menu.add_separator()

    view_menu.add_command(label="Problems")
    view_menu.add_command(label="Output")
    view_menu.add_command(label="Debug Console")
    view_menu.add_command(label="Terminal")
    view_menu.add_separator()

    view_menu.add_command(label="Word Wrap")

    menubar.add_cascade(label="View", menu=view_menu)
    return view_menu