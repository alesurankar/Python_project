import tkinter as tk
from tkinter import messagebox
from gui.menu.commands import help_menu_cmd

    
def cmd(name):
    return lambda: dispatch(name)

def create_help_menu(root, menubar):
    help_menu = tk.Menu(menubar, tearoff=0)
    
    help_menu.add_command(label="Welcome", command=cmd("welcome"))
    help_menu.add_command(label="Show All Commands", command=cmd("show_all_commands"))
    help_menu.add_command(label="Documentation", command=cmd("documentation"))
    help_menu.add_command(label="Editor Playground", command=cmd("editor_playground"))
    help_menu.add_command(label="Open Walkthrough...", command=cmd("open_walkthrough"))
    help_menu.add_command(label="Show Release Notes", command=cmd("show_release_notes"))
    help_menu.add_command(label="Get Started with Accessibility Features", command=cmd("get_started_with_accessibility_features"))
    help_menu.add_command(label="Ask @vscode_fake", command=cmd("ask_vscode_fake"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Keyboard Shortcuts Reference", command=cmd("keyboard_shortcuts_reference"))
    help_menu.add_command(label="Video Tutorials", command=cmd("video_tutorials"))
    help_menu.add_command(label="Tips and Tricks", command=cmd("tips_and_tricks"))
    help_menu.add_separator()

    help_menu.add_command(label="Join Us on YouTube", command=cmd("join_us_on_youtube"))
    help_menu.add_command(label="Search Feature Requests", command=cmd("search_feature_requests"))
    help_menu.add_command(label="Report Issue", command=cmd("report_issue"))
    help_menu.add_separator()
    
    help_menu.add_command(label="View License", command=cmd("view_license"))
    help_menu.add_command(label="Privacy Statement", command=cmd("privacy_statement"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Toggle Developer Tools", command=cmd("toggle_developer_tools"))
    help_menu.add_command(label="Open Process Explorer", command=cmd("open_process_explorer"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Check for Updates...", command=cmd("check_for_updates"))
    help_menu.add_separator()

    help_menu.add_command(label="About", command=cmd("about"))

    menubar.add_cascade(label="Help", menu=help_menu)
    return help_menu


def dispatch(action):
    func = getattr(help_menu_cmd, action, None)

    if callable(func):
        func(action)
    else:
        messagebox.showinfo("Info", f"Function '{action}' does not exist.")
