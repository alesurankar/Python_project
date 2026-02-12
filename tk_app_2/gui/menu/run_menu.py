import tkinter as tk
from gui.menu.commands import run_cmd
from gui.menu.helper import menu_helpers as helper


def create_run_menu(root, menubar):
    run_menu = tk.Menu(menubar, tearoff=0)
    
    run_menu.add_command(label="Start Debugging", command=helper.cmd("start_debugging", run_cmd))
    run_menu.add_command(label="Run Without Debugging", command=helper.cmd("run_without_debugging", run_cmd))
    run_menu.add_command(label="Stop Debugging", command=helper.cmd("stop_debugging", run_cmd), state="disabled")
    run_menu.add_command(label="Restart Debugging", command=helper.cmd("restart_debugging", run_cmd), state="disabled")
    run_menu.add_separator()

    run_menu.add_command(label="Open Configurations", command=helper.cmd("open_configurations", run_cmd), state="disabled")
    run_menu.add_command(label="Add Configurations...", command=helper.cmd("add_configurations", run_cmd))
    run_menu.add_separator()
    
    run_menu.add_command(label="Step Over", state="disabled", command=helper.cmd("step_over", run_cmd))
    run_menu.add_command(label="Step Into", state="disabled", command=helper.cmd("step_into", run_cmd))
    run_menu.add_command(label="Step Out", state="disabled", command=helper.cmd("step_out", run_cmd))
    run_menu.add_command(label="Continue", state="disabled", command=helper.cmd("continue_", run_cmd))
    run_menu.add_separator()

    run_menu.add_command(label="Toggle Breakpoint", command=helper.cmd("toggle_breakpoint", run_cmd))
    run_menu.add_command(label="New Breakpoint", command=helper.cmd("new_breakpoint", run_cmd))
    run_menu.add_separator()

    run_menu.add_command(label="Enable All Breakpoints", command=helper.cmd("enable_all_breakpoints", run_cmd))
    run_menu.add_command(label="Disable All Breakpoints", command=helper.cmd("disable_all_breakpoints", run_cmd))
    run_menu.add_command(label="Remove All Breakpoints", command=helper.cmd("remove_all_breakpoints", run_cmd))
    run_menu.add_separator()
    
    run_menu.add_command(label="Install Additional Debuggers...", command=helper.cmd("install_additional_debuggers", run_cmd))

    menubar.add_cascade(label="Run", menu=run_menu)
    return run_menu
