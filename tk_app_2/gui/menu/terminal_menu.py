import tkinter as tk
from gui.menu.commands import terminal_cmd
from gui.menu.helper import menu_helpers as helper

    
def create_terminal_menu(root, theme, menubar):
    terminal_menu = tk.Menu(
        menubar,
        tearoff=0,
        bg=theme.get("menu_bg"),
        fg=theme.get("menu_text"),
        activebackground=theme.get("menu_bg_hover"),
        activeforeground=theme.get("menu_text_hover"),
    )

    terminal_menu.add_command(label="New Terminal", command=helper.cmd("new_terminal", terminal_cmd))
    terminal_menu.add_command(label="Split Terminal", command=helper.cmd("split_terminal", terminal_cmd))
    terminal_menu.add_command(label="New Terminal Window", command=helper.cmd("new_terminal_window", terminal_cmd))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Run Task...", command=helper.cmd("run_task", terminal_cmd))
    terminal_menu.add_command(label="Run Build Task...", command=helper.cmd("run_build_task", terminal_cmd))
    terminal_menu.add_command(label="Run Active File...", command=helper.cmd("run_active_file", terminal_cmd))
    terminal_menu.add_command(label="Run Selected Text...", command=helper.cmd("run_selected_text", terminal_cmd))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Show Running Tasks...", command=helper.cmd("show_running_tasks", terminal_cmd))
    terminal_menu.add_command(label="Restart Running Task...", command=helper.cmd("restart_running_task", terminal_cmd))
    terminal_menu.add_command(label="Terminate Task...", command=helper.cmd("terminate_task", terminal_cmd))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Configure Tasks...", command=helper.cmd("configure_tasks", terminal_cmd))
    terminal_menu.add_command(label="Configure Default Build Task...", command=helper.cmd("configure_default_build_task", terminal_cmd))

    menubar.add_cascade(label="Terminal", menu=terminal_menu)
    return terminal_menu
