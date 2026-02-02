import os
import tkinter as tk
from tkinter import messagebox, filedialog
from data.data import Data


def create_menus(root, app):
    """Builds the main menu bar using the App instance."""
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    _build_menu(menubar, "File", FILE_MENU_ITEMS, app)
    _build_menu(menubar, "Help", HELP_MENU_ITEMS, app)


# Menu Builder
def _build_menu(menubar, label, items, app=None):
    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=label, menu=menu)

    for text, action in items:
            menu.add_command(label=text, command=lambda a=action: a(app))

    return menu


# Internal Menu
def _export_png(app):
    """Export current graph to PNG"""
    if not app.graph_widget or not hasattr(app.graph_widget, "fig"):
        messagebox.showwarning("Warning", "No graph to export!")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        title="Save Graph as PNG"
    )
    if file_path:
        app.graph_widget.fig.savefig(file_path, dpi=300, bbox_inches="tight")
        messagebox.showinfo("Saved", f"Graph saved to:\n{file_path}")

def _show_about(app=None):
    messagebox.showinfo("About", "Analysis App\nVersion 1.0")

def _load_new_data(app):
    """Load new CSV data into the App instance."""
    csv_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV files", "*.csv")]
    )
    if not csv_path:
        return
    
    meta_path = csv_path.replace(".csv", ".meta.json")
    if not os.path.exists(meta_path):
        meta_path = None
        
    app.data = Data(csv_path, meta_path)
    # Refresh graph
    if hasattr(app, "show_graph") and callable(app.show_graph):
        app.show_graph()


# Items
FILE_MENU_ITEMS = [
    ("Load Data...", _load_new_data),
    ("Export as PNG", _export_png),
    ("Exit", lambda app: app.root.quit()),
]

HELP_MENU_ITEMS = [
    ("About", _show_about),
]