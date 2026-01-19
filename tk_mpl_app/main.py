import os
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Import your plotting functions
from plot import draw_line, draw_bar

# -----------------------------
# Tkinter setup
# -----------------------------
root = tk.Tk()
root.title("Analysis App")
root.geometry("800x600")
icon_path = os.path.join("assets", 'icon.ico')
root.iconbitmap(icon_path)

# -----------------------------
# File menu
# -----------------------------
menubar = tk.Menu(root)
root.config(menu=menubar)
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Export (PNG)", command=lambda: print("Exporting PNG..."))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# -----------------------------
# View menu
# -----------------------------
view_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Line Chart", command=lambda: show_graph(0))
view_menu.add_command(label="Bar Chart", command=lambda: show_graph(1))

# -----------------------------
# Help menu
# -----------------------------
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
def show_about():
    tk.messagebox.showinfo("About", "Analysis App\nVersion 1.0")
help_menu.add_command(label="About", command=show_about)

# -----------------------------
# Top frame for controls
# -----------------------------
top_frame = ttk.Frame(root, padding=6)
top_frame.pack(side=tk.TOP, fill=tk.X)

# Buttons for navigation
graph_types = ['line', 'bar']
current = 0

# -----------------------------
# Plot frame
# -----------------------------
plot_frame = ttk.Frame(root, padding=6)
plot_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create Matplotlib figure
fig = plt.Figure(figsize=(8,5))
canvas = FigureCanvasTkAgg(fig, master=plot_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# -----------------------------
# Functions to switch graphs
# -----------------------------
def show_graph(index):
    global current
    current = index % len(graph_types)
    graph_func = draw_line if graph_types[current] == 'line' else draw_bar
    graph_func(fig)
    canvas.draw()

def next_graph():
    show_graph(current + 1)

def prev_graph():
    show_graph(current - 1)

# Buttons
prev_btn = ttk.Button(top_frame, text="Previous Graph", command=prev_graph)
prev_btn.pack(side=tk.RIGHT, padx=5)
next_btn = ttk.Button(top_frame, text="Next Graph", command=next_graph)
next_btn.pack(side=tk.RIGHT, padx=5)

# -----------------------------
# Show first graph
# -----------------------------
show_graph(0)

# -----------------------------
# Run main loop
# -----------------------------
root.mainloop()
