import tkinter as tk
from gui.menu.commands import file_cmd
from gui.menu.helper import menu_helpers as helper


def create_file_menu(root, theme, menubar):
    file_menu = tk.Menu(
        menubar,
        tearoff=0,
        bg=theme.get("menu_bg"),
        fg=theme.get("menu_text"),
        activebackground=theme.get("menu_bg_hover"),
        activeforeground=theme.get("menu_text_hover"),
    )
    
    file_menu.add_command(label="New Text File", command=helper.cmd("new_text_file", file_cmd))
    file_menu.add_command(label="New File...", command=helper.cmd("new_file", file_cmd))
    file_menu.add_command(label="New Window", command=helper.cmd("new_window", file_cmd))
    # Submenu for "New Window with Profile"
    profile_menu = tk.Menu(file_menu, tearoff=0)
    profile_menu.add_command(label="New Profile...", command=helper.cmd("new_profile", file_cmd))
    file_menu.add_cascade(label="New Window with Profile", menu=profile_menu)
    file_menu.add_separator()
    
    file_menu.add_command(label="Open File...", command=helper.cmd("open_file", file_cmd))
    file_menu.add_command(label="Open Folder...", command=helper.cmd("open_folder", file_cmd))
    file_menu.add_command(label="Open Workspace from File...", command=helper.cmd("open_workspace_from_file", file_cmd))
    # Submenu for "Open Recent"
    recent_menu = tk.Menu(file_menu, tearoff=0)
    recent_menu.add_command(label="Reopen Closed Editor", command=helper.cmd("reopen_closed_editor", file_cmd))
    recent_menu.add_separator()
    recent_menu.add_command(label="More...", command=helper.cmd("more", file_cmd))
    recent_menu.add_separator()
    recent_menu.add_command(label="Clear Recently Opened...", command=helper.cmd("clear_recently_opened", file_cmd))
    file_menu.add_cascade(label="Open Recent", menu=recent_menu)
    file_menu.add_separator()

    file_menu.add_command(label="Add Folder to Workspace...", command=helper.cmd("add_folder_to_workspace", file_cmd))
    file_menu.add_command(label="Save Workspace As...", command=helper.cmd("save_workspace_as", file_cmd))
    file_menu.add_command(label="Duplicate Workspace", command=helper.cmd("duplicate_workspace", file_cmd))
    file_menu.add_separator()
    
    file_menu.add_command(label="Save", command=helper.cmd("save", file_cmd))
    file_menu.add_command(label="Save As..", command=helper.cmd("save_as", file_cmd))
    file_menu.add_command(label="Save All", command=helper.cmd("save_all", file_cmd))
    file_menu.add_separator()

    # Submenu for "Share"
    share_menu = tk.Menu(file_menu, tearoff=0)
    share_menu.add_command(label="Copy vscode_fake.dev Link", command=helper.cmd("copy_vscode_fake_link", file_cmd))
    share_menu.add_separator()
    share_menu.add_command(label="Export Profile (Default)...", command=helper.cmd("export_profile_defaults", file_cmd))
    file_menu.add_cascade(label="Share", menu=share_menu)
    file_menu.add_separator()
    
    file_menu.add_command(label="Auto Save")
    preferences_menu = tk.Menu(file_menu, tearoff=0)
    preferences_menu.add_command(label="Profiles", command=helper.cmd("profiles", file_cmd))
    preferences_menu.add_command(label="Settings", command=helper.cmd("settings", file_cmd))
    preferences_menu.add_command(label="Extensions", command=helper.cmd("extensions", file_cmd))
    preferences_menu.add_command(label="Keyboard Shortcuts", command=helper.cmd("keyboard_shortcuts", file_cmd))
    preferences_menu.add_command(label="Configure Snippets", command=helper.cmd("configure_snippets", file_cmd))
    preferences_menu.add_command(label="Tasks", command=helper.cmd("tasks", file_cmd))
    themes_menu = tk.Menu(file_menu, tearoff=0)
    themes_menu.add_command(label="Color Theme", command=helper.cmd("color_theme", file_cmd))
    themes_menu.add_command(label="File Icon Theme", command=helper.cmd("file_icon_theme", file_cmd))
    themes_menu.add_command(label="Product Icon Theme", command=helper.cmd("product_icon_theme", file_cmd))
    preferences_menu.add_cascade(label="Themes", menu=themes_menu)
    preferences_menu.add_separator()
    preferences_menu.add_command(label="Backup and Sync Settings...", command=helper.cmd("backup_and_sync_settings", file_cmd))
    preferences_menu.add_separator()
    preferences_menu.add_command(label="Online Service Settings...", command=helper.cmd("online_service_settings", file_cmd))
    file_menu.add_cascade(label="Preferences", menu=preferences_menu)
    file_menu.add_separator()
    
    file_menu.add_command(label="Revert File", command=helper.cmd("revert_file", file_cmd))
    file_menu.add_command(label="Close Editor", command=helper.cmd("close_editor", file_cmd))
    file_menu.add_command(label="Close Folder", command=helper.cmd("close_folder", file_cmd))
    file_menu.add_command(label="Close Window", command=helper.cmd("close_window", file_cmd))
    file_menu.add_separator()

    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    return file_menu
