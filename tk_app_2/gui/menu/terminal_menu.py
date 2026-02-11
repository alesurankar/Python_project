import tkinter as tk
from tkinter import messagebox

    
def create_terminal_menu(root, menubar):
    terminal_menu = tk.Menu(menubar, tearoff=0)

    terminal_menu.add_command(label="New Terminal", command=lambda: dispatch("new_terminal"))
    terminal_menu.add_command(label="Split Terminal", command=lambda: dispatch("split_terminal"))
    terminal_menu.add_command(label="New Terminal Window", command=lambda: dispatch("new_terminal_window"))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Run Task...", command=lambda: dispatch("run_task"))
    terminal_menu.add_command(label="Run Build Task...", command=lambda: dispatch("run_build_task"))
    terminal_menu.add_command(label="Run Active File...", command=lambda: dispatch("run_active_file"))
    terminal_menu.add_command(label="Run Selected Text...", command=lambda: dispatch("run_selected_text"))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Show Running Tasks...", command=lambda: dispatch("show_running_tasks"))
    terminal_menu.add_command(label="Restart Running Task...", command=lambda: dispatch("restart_running_task"))
    terminal_menu.add_command(label="Terminate Task...", command=lambda: dispatch("terminate_task"))
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Configure Tasks...", command=lambda: dispatch("configure_tasks"))
    terminal_menu.add_command(label="Configure Default Build Task...", command=lambda: dispatch("configure_default_build_task"))

    menubar.add_cascade(label="Terminal", menu=terminal_menu)
    return terminal_menu


def dispatch(action):
    messagebox.showinfo("Info", f"{action} (not implemented yet)")