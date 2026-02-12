import tkinter as tk
from tkinter import messagebox
from gui.menu.commands import view_cmd
from gui.menu.helper import menu_helpers


def cmd(name):
    return lambda: dispatch(name)

def create_view_menu(root, menubar):
    view_menu = tk.Menu(menubar, tearoff=0)
    view = menu_helpers.ensure_namespace(root, "view")

    view_menu.add_command(label="Command Palette...", command=cmd("command_palette"))
    view_menu.add_command(label="Open View...", command=cmd("open_view"))
    view_menu.add_separator()

    # Submenu for "Appearance"
    appearance_menu = tk.Menu(view_menu, tearoff=0)

    appearance_menu.add_command(label="Full Screen", command=cmd("full_screen"))
    appearance_menu.add_command(label="Zen Mode", command=cmd("zen_mode"))
    appearance_menu.add_command(label="Centered Layout", command=cmd("centered_layout"))
    appearance_menu.add_separator()

    view.appearance_menu_bar = tk.BooleanVar(master=root, value=True)
    view.appearance_primary_side = tk.BooleanVar(master=root, value=True)
    view.appearance_secondary_side = tk.BooleanVar(master=root, value=False)
    view.appearance_status_bar = tk.BooleanVar(master=root, value=True)
    view.appearance_panel = tk.BooleanVar(master=root, value=True)
    appearance_menu.add_checkbutton(label="Menu Bar", variable=view.appearance_menu_bar, command=cmd("menu_bar"))
    appearance_menu.add_checkbutton(label="Primary Side Bar", variable=view.appearance_primary_side, command=cmd("primary_side_bar"))
    appearance_menu.add_checkbutton(label="Secondary Side Bar", variable=view.appearance_secondary_side, command=cmd("secondary_side_bar"))
    appearance_menu.add_checkbutton(label="Status Bar", variable=view.appearance_status_bar, command=cmd("status_bar"))
    appearance_menu.add_checkbutton(label="Panel", variable=view.appearance_panel, command=cmd("panel"))
    appearance_menu.add_separator()

    appearance_menu.add_command(label="Move Primary Side Bar Right", command=cmd("move_primary_side_bar_right"))

    # Submenu for "Activity Bar Position"
    activity_bar_position_menu = tk.Menu(view_menu, tearoff=0)
    view.activity_bar_position = tk.StringVar(master=root, value="Default")
    activity_bar_position_menu.add_radiobutton(label="Default", variable=view.activity_bar_position, value="Default", command=cmd("activity_bar_position_default"))
    activity_bar_position_menu.add_radiobutton(label="Top", variable=view.activity_bar_position, value="Top", command=cmd("activity_bar_position_top"))
    activity_bar_position_menu.add_radiobutton(label="Bottom", variable=view.activity_bar_position, value="Bottom", command=cmd("activity_bar_position_bottom"))
    activity_bar_position_menu.add_radiobutton(label="Hidden", variable=view.activity_bar_position, value="Hidden", command=cmd("activity_bar_position_hidden"))
    appearance_menu.add_cascade(label="Activity Bar Position", menu=activity_bar_position_menu)

    # Submenu for "Panel Position"
    panel_position_menu = tk.Menu(view_menu, tearoff=0)
    view.panel_position = tk.StringVar(master=root, value="Bottom")
    panel_position_menu.add_radiobutton(label="Top", variable=view.panel_position, value="Top", command=cmd("panel_position_top"))
    panel_position_menu.add_radiobutton(label="Left", variable=view.panel_position, value="Left", command=cmd("panel_position_left"))
    panel_position_menu.add_radiobutton(label="Right", variable=view.panel_position, value="Right", command=cmd("panel_position_right"))
    panel_position_menu.add_radiobutton(label="Bottom", variable=view.panel_position, value="Bottom", command=cmd("panel_position_bottom"))
    appearance_menu.add_cascade(label="Panel Position", menu=panel_position_menu)

    # Submenu for "Align Panel"
    align_panel_menu = tk.Menu(view_menu, tearoff=0)
    view.align_panel = tk.StringVar(master=root, value="Right")
    align_panel_menu.add_radiobutton(label="Center", variable=view.align_panel, value="Center", command=cmd("align_panel_center"))
    align_panel_menu.add_radiobutton(label="Justify", variable=view.align_panel, value="Justify", command=cmd("align_panel_justify"))
    align_panel_menu.add_radiobutton(label="Left", variable=view.align_panel, value="Left", command=cmd("align_panel_left"))
    align_panel_menu.add_radiobutton(label="Right", variable=view.align_panel, value="Right", command=cmd("align_panel_right"))
    appearance_menu.add_cascade(label="Align Panel", menu=align_panel_menu)

    # Submenu for "Tab Bar"
    tab_bar_menu = tk.Menu(view_menu, tearoff=0)
    view.tab_bar = tk.StringVar(master=root, value="Multiple Tabs")
    tab_bar_menu.add_radiobutton(label="Multiple Tabs", variable=view.tab_bar, value="Multiple Tabs", command=cmd("tab_bar_multiple_tabs"))
    tab_bar_menu.add_radiobutton(label="Single Tab", variable=view.tab_bar, value="Single Tab", command=cmd("tab_bar_single_tab"))
    tab_bar_menu.add_radiobutton(label="Hidden", variable=view.tab_bar, value="Hidden", command=cmd("tab_bar_hidden"))
    appearance_menu.add_cascade(label="Tab Bar", menu=tab_bar_menu)

    # Submenu for "Editor Actions Position"
    editor_actions_position_menu = tk.Menu(view_menu, tearoff=0)
    view.editor_actions_position = tk.StringVar(master=root, value="Tab Bar")
    editor_actions_position_menu.add_radiobutton(label="Tab Bar", variable=view.editor_actions_position, value="Tab Bar", command=cmd("editor_actions_position_tab_bar"))
    editor_actions_position_menu.add_radiobutton(label="Title Bar", variable=view.editor_actions_position, value="Title Bar", command=cmd("editor_actions_position_title_bar"))
    editor_actions_position_menu.add_radiobutton(label="Hidden", variable=view.editor_actions_position, value="Hidden", command=cmd("editor_actions_position_hidden"))
    appearance_menu.add_cascade(label="Editor Actions Position", menu=editor_actions_position_menu)
    appearance_menu.add_separator()

    view.appearance_minimap = tk.BooleanVar(master=root, value=False)
    view.appearance_breadcrumbs = tk.BooleanVar(master=root, value=True)
    view.appearance_sticky_scroll = tk.BooleanVar(master=root, value=True)
    view.appearance_render_whitespace = tk.BooleanVar(master=root, value=True)
    view.appearance_render_control_characters = tk.BooleanVar(master=root, value=True)
    appearance_menu.add_checkbutton(label="Minimap", variable=view.appearance_minimap, command=cmd("minimap"))
    appearance_menu.add_checkbutton(label="Breadcrumbs", variable=view.appearance_breadcrumbs, command=cmd("breadcrumbs"))
    appearance_menu.add_checkbutton(label="Sticky Scroll", variable=view.appearance_sticky_scroll, command=cmd("sticky_scroll"))
    appearance_menu.add_checkbutton(label="Render Whitespace", variable=view.appearance_render_whitespace, command=cmd("render_whitespace"))
    appearance_menu.add_checkbutton(label="Render Control Characters", variable=view.appearance_render_control_characters, command=cmd("render_control_characters"))
    appearance_menu.add_separator()

    appearance_menu.add_command(label="Zoom In", command=cmd("zoom_in"))
    appearance_menu.add_command(label="Zoom Out", command=cmd("zoom_out"))
    appearance_menu.add_command(label="Reset Zoom", command=cmd("reset_zoom"))
    # End Submenu for "Appearance"

    view_menu.add_cascade(label="Appearance", menu=appearance_menu)
    
    # Submenu for "Editor Layout"
    editor_layout_menu = tk.Menu(view_menu, tearoff=0)

    editor_layout_menu.add_command(label="Split Up", command=cmd("split_up"))
    editor_layout_menu.add_command(label="Split Down", command=cmd("split_down"))
    editor_layout_menu.add_command(label="Split Left", command=cmd("split_left"))
    editor_layout_menu.add_command(label="Split Right", command=cmd("split_right"))
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Split in Group", command=cmd("split_in_group"))
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Move Editor into New Window", command=cmd("move_editor_into_new_window"))
    editor_layout_menu.add_command(label="Copy Editor into New Window", command=cmd("copy_editor_into_new_window"))
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Single", command=cmd("single"))
    editor_layout_menu.add_command(label="Two Columns", command=cmd("two_columns"))
    editor_layout_menu.add_command(label="Three Columns", command=cmd("three_columns"))
    editor_layout_menu.add_command(label="Two Rows", command=cmd("two_rows"))
    editor_layout_menu.add_command(label="Three Rows", command=cmd("three_rows"))
    editor_layout_menu.add_command(label="Grid (2x2)", command=cmd("grid_2x2"))
    editor_layout_menu.add_command(label="Two Rows Right", command=cmd("two_rows_right"))
    editor_layout_menu.add_command(label="Two Columns Bottom", command=cmd("two_columns_bottom"))
    editor_layout_menu.add_separator()

    editor_layout_menu.add_command(label="Flip Layout", command=cmd("flip_layout"))
    # End Submenu for "Editor Layout"

    view_menu.add_cascade(label="Editor Layout", menu=editor_layout_menu)
    view_menu.add_separator()

    view_menu.add_command(label="Explorer", command=cmd("explorer"))
    view_menu.add_command(label="Search", command=cmd("search"))
    view_menu.add_command(label="Source Control", command=cmd("source_control"))
    view_menu.add_command(label="Run", command=cmd("run_view"))
    view_menu.add_command(label="Extensions", command=cmd("extensions"))
    view_menu.add_command(label="Testing", command=cmd("testing"))
    view_menu.add_separator()

    view_menu.add_command(label="Problems", command=cmd("problems"))
    view_menu.add_command(label="Output", command=cmd("output"))
    view_menu.add_command(label="Debug Console", command=cmd("debug_console"))
    view_menu.add_command(label="Terminal", command=cmd("terminal"))
    view_menu.add_separator()

    view_menu.add_command(label="Word Wrap", command=cmd("word_wrap"))

    menubar.add_cascade(label="View", menu=view_menu)
    return view_menu


def dispatch(action):
    func = getattr(view_cmd, action, None)

    if not callable(func):
        messagebox.showinfo("Info", f"Function '{action}' does not exist.")
        print("❌ Missing function:", action)
        return

    try:
        func(action)
    except TypeError:
        func()