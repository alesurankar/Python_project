import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def CreateGui(root):
    fig = plt.Figure(figsize=(8, 5))
    plot_frame = ttk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    return fig, canvas

# -----------------------------
# File menu
# -----------------------------


# -----------------------------
# View menu
# -----------------------------


# -----------------------------
# Help menu
# -----------------------------