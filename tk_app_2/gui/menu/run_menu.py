import tkinter as tk
from tkinter import messagebox


def create_run_menu(root, menubar):
    run_menu = tk.Menu(menubar, tearoff=0)
    
    run_menu.add_command(label="Start Debugging")
    run_menu.add_command(label="Run Without Debugging")
    run_menu.add_command(label="Stop Debugging", state="disabled")
    run_menu.add_command(label="Restart Debugging", state="disabled")
    run_menu.add_separator()

    run_menu.add_command(label="Open Configurations", state="disabled")
    run_menu.add_command(label="Add Configurations...")
    run_menu.add_separator()
    
    run_menu.add_command(label="Step Over", state="disabled")
    run_menu.add_command(label="Step Into", state="disabled")
    run_menu.add_command(label="Step Out", state="disabled")
    run_menu.add_command(label="continue", state="disabled")
    run_menu.add_separator()

    run_menu.add_command(label="Toggle Breakpoint")
    run_menu.add_command(label="New Breakpoint")
    run_menu.add_separator()

    run_menu.add_command(label="Enable All Breakpoints")
    run_menu.add_command(label="Disable All Breakpoints")
    run_menu.add_command(label="Remove All Breakpoints")
    run_menu.add_separator()
    
    run_menu.add_command(label="Install Additional Debuggers...")

    menubar.add_cascade(label="Run", menu=run_menu)
    return run_menu


def placeholder(action):
    messagebox.showinfo("Info", f"{action} (not implemented yet)")