import tkinter as tk


def create_run_menu(root, menubar):
    # Run menu
    run_menu = tk.Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Run", menu=run_menu)
    return run_menu