import tkinter as tk
from tkinter import messagebox
from gui.menu.commands import run_menu_cmd


def cmd(name):
    return lambda: dispatch(name)

def create_run_menu(root, menubar):
    run_menu = tk.Menu(menubar, tearoff=0)
    
    run_menu.add_command(label="Start Debugging", command=cmd("start_debugging"))
    run_menu.add_command(label="Run Without Debugging", command=cmd("run_without_debugging"))
    run_menu.add_command(label="Stop Debugging", command=cmd("stop_debugging"), state="disabled")
    run_menu.add_command(label="Restart Debugging", command=cmd("restart_debugging"), state="disabled")
    run_menu.add_separator()

    run_menu.add_command(label="Open Configurations", command=cmd("open_configurations"), state="disabled")
    run_menu.add_command(label="Add Configurations...", command=cmd("add_configurations"))
    run_menu.add_separator()
    
    run_menu.add_command(label="Step Over", state="disabled", command=cmd("step_over"))
    run_menu.add_command(label="Step Into", state="disabled", command=cmd("step_into"))
    run_menu.add_command(label="Step Out", state="disabled", command=cmd("step_out"))
    run_menu.add_command(label="Continue", state="disabled", command=cmd("continue_"))
    run_menu.add_separator()

    run_menu.add_command(label="Toggle Breakpoint", command=cmd("toggle_breakpoint"))
    run_menu.add_command(label="New Breakpoint", command=cmd("new_breakpoint"))
    run_menu.add_separator()

    run_menu.add_command(label="Enable All Breakpoints", command=cmd("enable_all_breakpoints"))
    run_menu.add_command(label="Disable All Breakpoints", command=cmd("disable_all_breakpoints"))
    run_menu.add_command(label="Remove All Breakpoints", command=cmd("remove_all_breakpoints"))
    run_menu.add_separator()
    
    run_menu.add_command(label="Install Additional Debuggers...", command=cmd("install_additional_debuggers"))

    menubar.add_cascade(label="Run", menu=run_menu)
    return run_menu


def dispatch(action):
    func = getattr(run_menu_cmd, action, None)

    if callable(func):
        func(action)
    else:
        messagebox.showinfo("Info", f"Function '{action}' does not exist.")