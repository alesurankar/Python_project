import tkinter as tk
from tkinter import messagebox, filedialog

def CreateMenus(root, fig):
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    
    _CreateFileMenu(root, menubar, fig)
    _CreateViewMenu(menubar)
    _CreateHelpMenu(menubar)


def _CreateFileMenu(root, menubar, fig):
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)

    def _ExportPNG():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )
        if file_path:
            fig.savefig(file_path, dpi=300, bbox_inches="tight")

    file_menu.add_command(label="Export as PNG", command=_ExportPNG)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    return file_menu

def _CreateViewMenu(menubar):
    view_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="View", menu=view_menu)
    return view_menu

def _CreateHelpMenu(menubar):
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)

    def _ShowAbout():
        messagebox.showinfo("About", "Analysis App\nVersion 1.0")

    help_menu.add_command(label="About", command=_ShowAbout)
    return help_menu