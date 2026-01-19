import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from plot import DrawLine, DrawBar


def CreateGui(root):
    # -----------------------------
    # Plot area
    # -----------------------------
    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    fig = plt.Figure(figsize=(8, 5))
    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # -----------------------------
    # Graph functions
    # -----------------------------
    def ShowLine():
        DrawLine(fig)
        canvas.draw()

    def ShowBar():
        DrawBar(fig)
        canvas.draw()

    # -----------------------------
    # File menu
    # -----------------------------
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    def ExportPNG():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )
        if file_path:
            fig.savefig(file_path, dpi=300, bbox_inches="tight")

    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Export as PNG", command=ExportPNG)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)

    # -----------------------------
    # View menu
    # -----------------------------
    view_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="View", menu=view_menu)
    view_menu.add_command(label="Show Line Graph", command=ShowLine)
    view_menu.add_command(label="Show Bar Chart", command=ShowBar)

    # -----------------------------
    # Help menu
    # -----------------------------
    help_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=help_menu)
    def ShowAbout():
        messagebox.showinfo("About", "Analysis App\nVersion 1.0")

    help_menu.add_command(label="About", command=ShowAbout)

    # -----------------------------
    # Top buttons for navigation
    # -----------------------------
    top_frame = ttk.Frame(root, padding=5)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    prev_button = ttk.Button(top_frame, text="Previous", command=lambda: ShowLine())
    prev_button.pack(side=tk.RIGHT, padx=5)
    next_button = ttk.Button(top_frame, text="Next", command=lambda: ShowBar())
    next_button.pack(side=tk.RIGHT, padx=5)

    # -----------------------------
    # Show initial graph
    # -----------------------------
    ShowLine()

    # Return figure and canvas in case app.py wants it
    return fig, canvas