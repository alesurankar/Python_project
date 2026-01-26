import tkinter as tk
from tkinter import messagebox, filedialog


def CreateMenus(root, fig):
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    _BuildMenu(menubar, "File", FILE_MENU_ITEMS, {"root": root, "fig": fig})
    _BuildMenu(menubar, "Help", HELP_MENU_ITEMS)


# Menu Builder
def _BuildMenu(menubar, label, items, context=None):
    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label=label, menu=menu)

    for text, action in items:
        if context is not None:
            menu.add_command(label=text, command=lambda a=action: a(context))
        else:
            menu.add_command(label=text, command=action)
    return menu

# Internal Menu
def _ExportPNG(fig):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )
    if file_path:
        fig.savefig(file_path, dpi=300, bbox_inches="tight")

def _ShowAbout():
    messagebox.showinfo("About", "Analysis App\nVersion 1.0")

# Items
FILE_MENU_ITEMS = [
    ("Export as PNG", lambda ctx: _ExportPNG(ctx["fig"])),
    ("Exit", lambda ctx: ctx["root"].quit()),
]

HELP_MENU_ITEMS = [
    ("About", _ShowAbout),
]