import tkinter as tk
from tkinter import messagebox


def create_file_menu(root, menubar):
    file_menu = tk.Menu(menubar, tearoff=0)
    
    file_menu.add_command(label="New Text File")
    file_menu.add_command(label="New File...")
    file_menu.add_command(label="New Window")
    # Submenu for "New Window with Profile"
    profile_menu = tk.Menu(file_menu, tearoff=0)
    profile_menu.add_command(label="New Profile...")
    file_menu.add_cascade(label="New Window with Profile", menu=profile_menu)
    file_menu.add_separator()
    
    file_menu.add_command(label="Open File...")
    file_menu.add_command(label="Open Folder...")
    file_menu.add_command(label="Open Workspace from File...")
    # Submenu for "Open Recent"
    recent_menu = tk.Menu(file_menu, tearoff=0)
    recent_menu.add_command(label="Reopen Closed Editor")
    recent_menu.add_separator()
    recent_menu.add_command(label="More...")
    recent_menu.add_separator()
    recent_menu.add_command(label="Clear Recently Opened...")
    file_menu.add_cascade(label="Open Recent", menu=recent_menu)
    file_menu.add_separator()

    file_menu.add_command(label="Add Folder to Workspace...")
    file_menu.add_command(label="Save Workspace As...")
    file_menu.add_command(label="Duplicate Workspace")
    file_menu.add_separator()
    
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Save As..")
    file_menu.add_command(label="Save All")
    file_menu.add_separator()

    # Submenu for "Share"
    share_menu = tk.Menu(file_menu, tearoff=0)
    share_menu.add_command(label="Copy vscode.dev Link")
    share_menu.add_separator()
    share_menu.add_command(label="Export Profile (Default)...")
    file_menu.add_cascade(label="Share", menu=share_menu)
    file_menu.add_separator()
    
    file_menu.add_command(label="Auto Save")
    preferences_menu = tk.Menu(file_menu, tearoff=0)
    preferences_menu.add_command(label="Profiles")
    preferences_menu.add_command(label="Settings")
    preferences_menu.add_command(label="Extensions")
    preferences_menu.add_command(label="Keyboard Shortcuts")
    preferences_menu.add_command(label="Configure Snippets")
    preferences_menu.add_command(label="Tasks")
    themes_menu = tk.Menu(file_menu, tearoff=0)
    themes_menu.add_command(label="Color Theme")
    themes_menu.add_command(label="File Icon Theme")
    themes_menu.add_command(label="Product Icon Theme")
    preferences_menu.add_cascade(label="Themes", menu=themes_menu)
    preferences_menu.add_separator()
    preferences_menu.add_command(label="Backup and Sync Settings...")
    preferences_menu.add_separator()
    preferences_menu.add_command(label="Online Service Settings...")
    file_menu.add_cascade(label="Preferences", menu=preferences_menu)
    file_menu.add_separator()
    
    file_menu.add_command(label="Revert File")
    file_menu.add_command(label="Close Editor")
    file_menu.add_command(label="Close Folder")
    file_menu.add_command(label="Close Window")
    file_menu.add_separator()

    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)
    return file_menu


def placeholder(action):
    messagebox.showinfo("Info", f"{action} (not implemented yet)")