from tkinter import filedialog, messagebox
from plot import DrawLine, DrawBar

graphs = [DrawLine, DrawBar]
current = 0

def ShowGraph(fig, canvas, index):
    global current
    current = index % len(graphs)
    graphs[current](fig)
    canvas.draw()

def ExportPNG(fig):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")]
    )
    if file_path:
        fig.savefig(file_path, dpi=300, bbox_inches="tight")

def ShowAbout():
    messagebox.showinfo("About", "Analysis App\nVersion 1.0")