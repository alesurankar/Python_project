import tkinter as tk
from tkinter import messagebox
from gui.menu.commands import help_menu_cmd

    
def create_help_menu(root, menubar):
    help_menu = tk.Menu(menubar, tearoff=0)
    
    help_menu.add_command(label="Welcome", command=lambda: dispatch("welcome"))
    help_menu.add_command(label="Show All Commands", command=lambda: dispatch("show_all_commands"))
    help_menu.add_command(label="Documentation", command=lambda: dispatch("documentation"))
    help_menu.add_command(label="Editor Playground", command=lambda: dispatch("editor_playground"))
    help_menu.add_command(label="Open Walkthrough...", command=lambda: dispatch("open_walkthrough"))
    help_menu.add_command(label="Show Release Notes", command=lambda: dispatch("show_release_notes"))
    help_menu.add_command(label="Get Started with Accessibility Features", command=lambda: dispatch("get_started_with_accessibility_features"))
    help_menu.add_command(label="Ask @vscode_fake", command=lambda: dispatch("ask_vscode_fake"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Keyboard Shortcuts Reference", command=lambda: dispatch("keyboard_shortcuts_reference"))
    help_menu.add_command(label="Video Tutorials", command=lambda: dispatch("video_tutorials"))
    help_menu.add_command(label="tips and Tricks", command=lambda: dispatch("tips_and_tricks"))
    help_menu.add_separator()

    help_menu.add_command(label="Join Us on YouTube", command=lambda: dispatch("join_us_on_youtube"))
    help_menu.add_command(label="Search Feature Requests", command=lambda: dispatch("search_feature_requests"))
    help_menu.add_command(label="Report Issue", command=lambda: dispatch("report_issue"))
    help_menu.add_separator()
    
    help_menu.add_command(label="View License", command=lambda: dispatch("view_license"))
    help_menu.add_command(label="Privacy Statement", command=lambda: dispatch("privacy_statement"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Toggle Developer Tools", command=lambda: dispatch("toggle_developer_tools"))
    help_menu.add_command(label="Open Process Explorer", command=lambda: dispatch("open_process_explorer"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Check for Updates...", command=lambda: dispatch("check_for_updates"))
    help_menu.add_separator()

    help_menu.add_command(label="About", command=lambda: dispatch("about"))

    menubar.add_cascade(label="Help", menu=help_menu)
    return help_menu


def dispatch(action):
    func = getattr(help_menu_cmd, action, None)

    if callable(func):
        func()
    else:
        messagebox.showinfo("Info", f"{action} (not implemented yet)")
