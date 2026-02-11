import tkinter as tk
from tkinter import messagebox

    
def create_help_menu(root, menubar):
    help_menu = tk.Menu(menubar, tearoff=0)
    
    help_menu.add_command(label="Welcome", command=lambda: placeholder("welcome"))
    help_menu.add_command(label="Show All Commands", command=lambda: placeholder("show_all_commands"))
    help_menu.add_command(label="Documentation", command=lambda: placeholder("documentation"))
    help_menu.add_command(label="Editor Playground", command=lambda: placeholder("editor_playground"))
    help_menu.add_command(label="Open Walkthrough...", command=lambda: placeholder("open_walkthrough"))
    help_menu.add_command(label="Show Release Notes", command=lambda: placeholder("show_release_notes"))
    help_menu.add_command(label="Get Started with Accessibility Features", command=lambda: placeholder("get_started_with_accessibility_features"))
    help_menu.add_command(label="Ask @vscode_fake", command=lambda: placeholder("ask_vscode_fake"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Keyboard Shortcuts Reference", command=lambda: placeholder("keyboard_shortcuts_reference"))
    help_menu.add_command(label="Video Tutorials", command=lambda: placeholder("video_tutorials"))
    help_menu.add_command(label="tips and Tricks", command=lambda: placeholder("tips_and_tricks"))
    help_menu.add_separator()

    help_menu.add_command(label="Join Us on YouTube", command=lambda: placeholder("join_us_on_youtube"))
    help_menu.add_command(label="Search Feature Requests", command=lambda: placeholder("search_feature_requests"))
    help_menu.add_command(label="Report Issue", command=lambda: placeholder("report_issue"))
    help_menu.add_separator()
    
    help_menu.add_command(label="View License", command=lambda: placeholder("view_license"))
    help_menu.add_command(label="Privacy Statement", command=lambda: placeholder("privacy_statement"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Toggle Developer Tools", command=lambda: placeholder("toggle_developer_tools"))
    help_menu.add_command(label="Open Process Explorer", command=lambda: placeholder("open_process_explorer"))
    help_menu.add_separator()
    
    help_menu.add_command(label="Check for Updates...", command=lambda: placeholder("check_for_updates"))
    help_menu.add_separator()

    help_menu.add_command(label="About", command=lambda: placeholder("about"))

    menubar.add_cascade(label="Help", menu=help_menu)
    return help_menu


def placeholder(action):
    messagebox.showinfo("Info", f"{action} (not implemented yet)")
