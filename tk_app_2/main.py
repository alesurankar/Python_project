import os
import tkinter as tk
from state import AppState
from gui.menu_bar import MenuBar, MenuBar2
from gui.body_frame import BodyFrame
from gui.footer_bar import FooterBar


root = tk.Tk()
root.title("Visual Studio Code - fake")
root.geometry("800x600")
icon_path = os.path.join("assets", 'icon.ico')
root.iconbitmap(icon_path)
root.minsize(width=400, height=220)

state = AppState(root)
menu = MenuBar(root, state) 
menu2 = MenuBar2(root, state, 26) 
menu2.pack(side="top", fill="x") 
footer = FooterBar(root, state, 30) 
footer.pack(side="bottom", fill="x")  
body = BodyFrame(root, state)  
body.pack(fill="both", expand=True)


root.mainloop()
