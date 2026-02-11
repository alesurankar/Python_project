import tkinter as tk


class MenuBar:
    def __init__(self, root, state):
        self.root = root
        self.state = state

        menubar = tk.Menu(root)
        root.config(menu=menubar)

        self.file_menu = self.create_file_menu(menubar)
        self.edit_menu = self.create_edit_menu(menubar)
        self.selection_menu = self.create_selection_menu(menubar)
        self.view_menu = self.create_view_menu(menubar)
        self.go_menu = self.create_go_menu(menubar)
        self.run_menu = self.create_run_menu(menubar)
        self.terminal_menu = self.create_terminal_menu(menubar)
        self.help_menu = self.create_help_menu(menubar)


    def create_file_menu(self, menubar):
        # File menu
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

        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        return file_menu

    def create_edit_menu(self, menubar):
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Undo")
        edit_menu.add_command(label="Redo")
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Paste")
        menubar.add_cascade(label="Edit", menu=edit_menu)
        return edit_menu

    def create_selection_menu(self, menubar):
        # Selection menu
        selection_menu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Selection", menu=selection_menu)
        return selection_menu

    def create_view_menu(self, menubar):
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="View", menu=view_menu)
        return view_menu

    def create_go_menu(self, menubar):
        # Go menu
        go_menu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Go", menu=go_menu)
        return go_menu

    def create_run_menu(self, menubar):
        # Run menu
        run_menu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Run", menu=run_menu)
        return run_menu
        
    def create_terminal_menu(self, menubar):
        # Terminal menu
        terminal_menu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label="Terminal", menu=terminal_menu)
        return terminal_menu
        
    def create_help_menu(self, menubar):
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About")

        menubar.add_cascade(label="Help", menu=help_menu)
        return help_menu