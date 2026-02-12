import tkinter as tk
from gui.menu.commands import view_cmd
from gui.menu.helper import menu_helpers as helper


def create_view_menu(root, menubar):
    view_menu = tk.Menu(menubar, tearoff=0)
    view = helper.ensure_namespace(root, "view")

    view_menu.add_command(label="Command Palette...", command=helper.cmd("command_palette", view_cmd))
    view_menu.add_command(label="Open View...", command=helper.cmd("open_view", view_cmd))
    view_menu.add_separator()

    # Submenu for "Appearance"
    appearance_menu = tk.Menu(view_menu, tearoff=0)

    appearance_menu.add_command(label="Full Screen", command=helper.cmd("full_screen", view_cmd))
    appearance_menu.add_command(label="Zen Mode", command=helper.cmd("zen_mode", view_cmd))
    appearance_menu.add_command(label="Centered Layout", command=helper.cmd("centered_layout", view_cmd))
    appearance_menu.add_separator()

    view.appearance_menu_bar = tk.BooleanVar(master=root, value=True)
    view.appearance_primary_side = tk.BooleanVar(master=root, value=True)
    view.appearance_secondary_side = tk.BooleanVar(master=root, value=False)
    view.appearance_status_bar = tk.BooleanVar(master=root, value=True)
    view.appearance_panel = tk.BooleanVar(master=root, value=True)
    appearance_menu.add_checkbutton(label="Menu Bar", variable=view.appearance_menu_bar, command=helper.cmd("menu_bar", view_cmd))
    appearance_menu.add_checkbutton(label="Primary Side Bar", variable=view.appearance_primary_side, command=helper.cmd("primary_side_bar", view_cmd))
    appearance_menu.add_checkbutton(label="Secondary Side Bar", variable=view.appearance_secondary_side, command=helper.cmd("secondary_side_bar", view_cmd))
    appearance_menu.add_checkbutton(label="Status Bar", variable=view.appearance_status_bar, command=helper.cmd("status_bar", view_cmd))
    appearance_menu.add_checkbutton(label="Panel", variable=view.appearance_panel, command=helper.cmd("panel", view_cmd))
    appearance_menu.add_separator()

    appearance_menu.add_command(label="Move Primary Side Bar Right", command=helper.cmd("move_primary_side_bar_right", view_cmd))

    # Submenu for "Activity Bar Position"
    activity_bar_position_menu = tk.Menu(view_menu, tearoff=0)
    view.activity_bar_position = tk.StringVar(master=root, value="Default")
    activity_bar_position_menu.add_radiobutton(label="Default", variable=view.activity_bar_position, value="Default", command=helper.cmd("activity_bar_position_default", view_cmd))
    activity_bar_position_menu.add_radiobutton(label="Top", variable=view.activity_bar_position, value="Top", command=helper.cmd("activity_bar_position_top", view_cmd))
    activity_bar_position_menu.add_radiobutton(label="Bottom", variable=view.activity_bar_position, value="Bottom", command=helper.cmd("activity_bar_position_bottom", view_cmd))
    activity_bar_position_menu.add_radiobutton(label="Hidden", variable=view.activity_bar_position, value="Hidden", command=helper.cmd("activity_bar_position_hidden", view_cmd))
    appearance_menu.add_cascade(label="Activity Bar Position", menu=activity_bar_position_menu)

    # Submenu for "Panel Position"
    panel_position_menu = tk.Menu(view_menu, tearoff=0)
    view.panel_position = tk.StringVar(master=root, value="Bottom")
    panel_position_menu.add_radiobutton(label="Top", variable=view.panel_position, value="Top", command=helper.cmd("panel_position_top", view_cmd))
    panel_position_menu.add_radiobutton(label="Left", variable=view.panel_position, value="Left", command=helper.cmd("panel_position_left", view_cmd))
    panel_position_menu.add_radiobutton(label="Right", variable=view.panel_position, value="Right", command=helper.cmd("panel_position_right", view_cmd))
    panel_position_menu.add_radiobutton(label="Bottom", variable=view.panel_position, value="Bottom", command=helper.cmd("panel_position_bottom", view_cmd))
    appearance_menu.add_cascade(label="Panel Position", menu=panel_position_menu)

    # Submenu for "Align Panel"
    align_panel_menu = tk.Menu(view_menu, tearoff=0)
    view.align_panel = tk.StringVar(master=root, value="Right")
    align_panel_menu.add_radiobutton(label="Center", variable=view.align_panel, value="Center", command=helper.cmd("align_panel_center", view_cmd))
    align_panel_menu.add_radiobutton(label="Justify", variable=view.align_panel, value="Justify", command=helper.cmd("align_panel_justify", view_cmd))
    align_panel_menu.add_radiobutton(label="Left", variable=view.align_panel, value="Left", command=helper.cmd("align_panel_left", view_cmd))
    align_panel_menu.add_radiobutton(label="Right", variable=view.align_panel, value="Right", command=helper.cmd("align_panel_right", view_cmd))
    appearance_menu.add_cascade(label="Align Panel", menu=align_panel_menu)

    # Submenu for "Tab Bar"
    tab_bar_menu = tk.Menu(view_menu, tearoff=0)
    view.tab_bar = tk.StringVar(master=root, value="Multiple Tabs")
    tab_bar_menu.add_radiobutton(label="Multiple Tabs", variable=view.tab_bar, value="Multiple Tabs", command=helper.cmd("tab_bar_multiple_tabs", view_cmd))
    tab_bar_menu.add_radiobutton(label="Single Tab", variable=view.tab_bar, value="Single Tab", command=helper.cmd("tab_bar_single_tab", view_cmd))
    tab_bar_menu.add_radiobutton(label="Hidden", variable=view.tab_bar, value="Hidden", command=helper.cmd("tab_bar_hidden", view_cmd))
    appearance_menu.add_cascade(label="Tab Bar", menu=tab_bar_menu)

    # Submenu for "Editor Actions Position"
    editor_actions_position_menu = tk.Menu(view_menu, tearoff=0)
    view.editor_actions_position = tk.StringVar(master=root, value="Tab Bar")
    editor_actions_position_menu.add_radiobutton(label="Tab Bar", variable=view.editor_actions_position, value="Tab Bar", command=helper.cmd("editor_actions_position_tab_bar", view_cmd))
    editor_actions_position_menu.add_radiobutton(label="Title Bar", variable=view.editor_actions_position, value="Title Bar", command=helper.cmd("editor_actions_position_title_bar", view_cmd))
    editor_actions_position_menu.add_radiobutton(label="Hidden", variable=view.editor_actions_position, value="Hidden", command=helper.cmd("editor_actions_position_hidden", view_cmd))
    appearance_menu.add_cascade(label="Editor Actions Position", menu=editor_actions_position_menu)
    appearance_menu.add_separator()

    view.appearance_minimap = tk.BooleanVar(master=root, value=False)
    view.appearance_breadcrumbs = tk.BooleanVar(master=root, value=True)
    view.appearance_sticky_scroll = tk.BooleanVar(master=root, value=True)
    view.appearance_render_whitespace = tk.BooleanVar(master=root, value=True)
    view.appearance_render_control_characters = tk.BooleanVar(master=root, value=True)
    appearance_menu.add_checkbutton(label="Minimap", variable=view.appearance_minimap, command=helper.cmd("minimap", view_cmd))
    appearance_menu.add_checkbutton(label="Breadcrumbs", variable=view.appearance_breadcrumbs, command=helper.cmd("breadcrumbs", view_cmd))
    appearance_menu.add_checkbutton(label="Sticky Scroll", variable=view.appearance_sticky_scroll, command=helper.cmd("sticky_scroll", view_cmd))
    appearance_menu.add_checkbutton(label="Render Whitespace", variable=view.appearance_render_whitespace, command=helper.cmd("render_whitespace", view_cmd))
    appearance_menu.add_checkbutton(label="Render Control Characters", variable=view.appearance_render_control_characters, command=helper.cmd("render_control_characters", view_cmd))
    appearance_menu.add_separator()

    appearance_menu.add_command(label="Zoom In", command=helper.cmd("zoom_in", view_cmd))
    appearance_menu.add_command(label="Zoom Out", command=helper.cmd("zoom_out", view_cmd))
    appearance_menu.add_command(label="Reset Zoom", command=helper.cmd("reset_zoom", view_cmd))
    # End Submenu for "Appearance"

    view_menu.add_cascade(label="Appearance", menu=appearance_menu)
    
    # Submenu for "Editor Layout"
    editor_layout_menu = tk.Menu(view_menu, tearoff=0)

    editor_layout_menu.add_command(label="Split Up", command=helper.cmd("split_up", view_cmd))
    editor_layout_menu.add_command(label="Split Down", command=helper.cmd("split_down", view_cmd))
    editor_layout_menu.add_command(label="Split Left", command=helper.cmd("split_left", view_cmd))
    editor_layout_menu.add_command(label="Split Right", command=helper.cmd("split_right", view_cmd))
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Split in Group", command=helper.cmd("split_in_group", view_cmd))
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Move Editor into New Window", command=helper.cmd("move_editor_into_new_window", view_cmd))
    editor_layout_menu.add_command(label="Copy Editor into New Window", command=helper.cmd("copy_editor_into_new_window", view_cmd))
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Single", command=helper.cmd("single", view_cmd))
    editor_layout_menu.add_command(label="Two Columns", command=helper.cmd("two_columns", view_cmd))
    editor_layout_menu.add_command(label="Three Columns", command=helper.cmd("three_columns", view_cmd))
    editor_layout_menu.add_command(label="Two Rows", command=helper.cmd("two_rows", view_cmd))
    editor_layout_menu.add_command(label="Three Rows", command=helper.cmd("three_rows", view_cmd))
    editor_layout_menu.add_command(label="Grid (2x2)", command=helper.cmd("grid_2x2", view_cmd))
    editor_layout_menu.add_command(label="Two Rows Right", command=helper.cmd("two_rows_right", view_cmd))
    editor_layout_menu.add_command(label="Two Columns Bottom", command=helper.cmd("two_columns_bottom", view_cmd))
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Flip Layout", command=helper.cmd("flip_layout", view_cmd))
    # End Submenu for "Editor Layout"

    view_menu.add_cascade(label="Editor Layout", menu=editor_layout_menu)
    view_menu.add_separator()

    view_menu.add_command(label="Explorer", command=helper.cmd("explorer", view_cmd))
    view_menu.add_command(label="Search", command=helper.cmd("search", view_cmd))
    view_menu.add_command(label="Source Control", command=helper.cmd("source_control", view_cmd))
    view_menu.add_command(label="Run", command=helper.cmd("run_view", view_cmd))
    view_menu.add_command(label="Extensions", command=helper.cmd("extensions", view_cmd))
    view_menu.add_command(label="Testing", command=helper.cmd("testing", view_cmd))
    view_menu.add_separator()

    view_menu.add_command(label="Problems", command=helper.cmd("problems", view_cmd))
    view_menu.add_command(label="Output", command=helper.cmd("output", view_cmd))
    view_menu.add_command(label="Debug Console", command=helper.cmd("debug_console", view_cmd))
    view_menu.add_command(label="Terminal", command=helper.cmd("terminal", view_cmd))
    view_menu.add_separator()

    view_menu.add_command(label="Word Wrap", command=helper.cmd("word_wrap", view_cmd))

    menubar.add_cascade(label="View", menu=view_menu)
    return view_menu
