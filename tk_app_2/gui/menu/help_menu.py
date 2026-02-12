import tkinter as tk
from gui.menu.commands import help_cmd
from gui.menu.helper import menu_helpers as helper


def create_help_menu(root, theme, menubar):
    help_menu = tk.Menu(
        menubar,
        tearoff=0,
        bg=theme.get("menu_bg"),
        fg=theme.get("menu_text"),
        activebackground=theme.get("menu_bg_hover"),
        activeforeground=theme.get("menu_text_hover"),
    )
    
    help_menu.add_command(label="Welcome", command=helper.cmd("welcome", help_cmd))
    help_menu.add_command(label="Show All Commands", command=helper.cmd("show_all_commands", help_cmd))
    help_menu.add_command(label="Documentation", command=helper.cmd("documentation", help_cmd))
    help_menu.add_command(label="Editor Playground", command=helper.cmd("editor_playground", help_cmd))
    help_menu.add_command(label="Open Walkthrough...", command=helper.cmd("open_walkthrough", help_cmd))
    help_menu.add_command(label="Show Release Notes", command=helper.cmd("show_release_notes", help_cmd))
    help_menu.add_command(label="Get Started with Accessibility Features", command=helper.cmd("get_started_with_accessibility_features", help_cmd))
    help_menu.add_command(label="Ask @vscode_fake", command=helper.cmd("ask_vscode_fake", help_cmd))
    help_menu.add_separator()
    
    help_menu.add_command(label="Keyboard Shortcuts Reference", command=helper.cmd("keyboard_shortcuts_reference", help_cmd))
    help_menu.add_command(label="Video Tutorials", command=helper.cmd("video_tutorials", help_cmd))
    help_menu.add_command(label="Tips and Tricks", command=helper.cmd("tips_and_tricks", help_cmd))
    help_menu.add_separator()

    help_menu.add_command(label="Join Us on YouTube", command=helper.cmd("join_us_on_youtube", help_cmd))
    help_menu.add_command(label="Search Feature Requests", command=helper.cmd("search_feature_requests", help_cmd))
    help_menu.add_command(label="Report Issue", command=helper.cmd("report_issue", help_cmd))
    help_menu.add_separator()
    
    help_menu.add_command(label="View License", command=helper.cmd("view_license", help_cmd))
    help_menu.add_command(label="Privacy Statement", command=helper.cmd("privacy_statement", help_cmd))
    help_menu.add_separator()
    
    help_menu.add_command(label="Toggle Developer Tools", command=helper.cmd("toggle_developer_tools", help_cmd))
    help_menu.add_command(label="Open Process Explorer", command=helper.cmd("open_process_explorer", help_cmd))
    help_menu.add_separator()
    
    help_menu.add_command(label="Check for Updates...", command=helper.cmd("check_for_updates", help_cmd))
    help_menu.add_separator()

    help_menu.add_command(label="About", command=helper.cmd("about", help_cmd))

    menubar.add_cascade(label="Help", menu=help_menu)
    return help_menu
