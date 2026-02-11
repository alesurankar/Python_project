import tkinter as tk

    
def create_terminal_menu(root, menubar):
    terminal_menu = tk.Menu(menubar, tearoff=0)

    terminal_menu.add_command(label="New Terminal")
    terminal_menu.add_command(label="Split Terminal")
    terminal_menu.add_command(label="New Terminal Window")
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Run Task...")
    terminal_menu.add_command(label="Run Build Task...")
    terminal_menu.add_command(label="Run Active File...")
    terminal_menu.add_command(label="Run Selected Text...")
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Show Running Tasks...")
    terminal_menu.add_command(label="Restart Running Task...")
    terminal_menu.add_command(label="Terminate Task...")
    terminal_menu.add_separator()
    
    terminal_menu.add_command(label="Configure Tasks...")
    terminal_menu.add_command(label="Configure Default Build Task...")

    menubar.add_cascade(label="Terminal", menu=terminal_menu)
    return terminal_menu