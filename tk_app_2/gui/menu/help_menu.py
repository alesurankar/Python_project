import tkinter as tk

    
def create_help_menu(root, menubar):
    help_menu = tk.Menu(menubar, tearoff=0)
    
    help_menu.add_command(label="Welcome")
    help_menu.add_command(label="Show All Commands")
    help_menu.add_command(label="Documentation")
    help_menu.add_command(label="Editor Playground")
    help_menu.add_command(label="Open Walkthrough...")
    help_menu.add_command(label="Show Release Notes")
    help_menu.add_command(label="Get Started with Accessibility Features")
    help_menu.add_command(label="Ask @vscode-fake")
    help_menu.add_separator()
    
    help_menu.add_command(label="Keyboard Shortcuts Reference")
    help_menu.add_command(label="Video Tutorials")
    help_menu.add_command(label="tips and Tricks")
    help_menu.add_separator()

    help_menu.add_command(label="Join Us on YouTube")
    help_menu.add_command(label="Search Feature Requests")
    help_menu.add_command(label="report Issue")
    help_menu.add_separator()
    
    help_menu.add_command(label="View License")
    help_menu.add_command(label="Privacy Statement")
    help_menu.add_separator()
    
    help_menu.add_command(label="Toggle Developer Tools")
    help_menu.add_command(label="Open Process Explorer")
    help_menu.add_separator()
    
    help_menu.add_command(label="Check for Updates...")
    help_menu.add_separator()

    help_menu.add_command(label="About")

    menubar.add_cascade(label="Help", menu=help_menu)
    return help_menu