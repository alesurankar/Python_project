import os
import tkinter as tk
from gui import CreateGui
from actions import ShowGraph, ExportPNG

root = tk.Tk()
root.title("Analysis App")
root.geometry("800x600")
icon_path = os.path.join("assets", 'icon.ico')
root.iconbitmap(icon_path)

fig, canvas = CreateGui(root)

ShowGraph(fig, canvas, 0)

root.mainloop()
