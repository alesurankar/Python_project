import tkinter as tk
from tkinter import messagebox
from gui.menu.commands import terminal_cmd


def cmd(name):
    return lambda: dispatch(name)
    
def create_terminal_menu(root, menubar):
    terminal_menu = tk.Menu(menubar, tearoff=0)

    terminal_menu.add_command(label="New Terminal", command=cmd("new_terminal"))
    terminal_menu.add_command(label="Split Terminal", command=cmd("split_terminal"))
    terminal_menu.add_command(label="New Terminal Window", command=cmd("new_terminal_window"))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Run Task...", command=cmd("run_task"))
    terminal_menu.add_command(label="Run Build Task...", command=cmd("run_build_task"))
    terminal_menu.add_command(label="Run Active File...", command=cmd("run_active_file"))
    terminal_menu.add_command(label="Run Selected Text...", command=cmd("run_selected_text"))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Show Running Tasks...", command=cmd("show_running_tasks"))
    terminal_menu.add_command(label="Restart Running Task...", command=cmd("restart_running_task"))
    terminal_menu.add_command(label="Terminate Task...", command=cmd("terminate_task"))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Configure Tasks...", command=cmd("configure_tasks"))
    terminal_menu.add_command(label="Configure Default Build Task...", command=cmd("configure_default_build_task"))

    menubar.add_cascade(label="Terminal", menu=terminal_menu)
    return terminal_menu


def dispatch(action):
    func = getattr(terminal_cmd, action, None)

    if not callable(func):
        messagebox.showinfo("Info", f"Function '{action}' does not exist.")
        print("❌ Missing function:", action)
        return

    try:
        func(action)
    except TypeError:
        func()