import tkinter as tk
from gui.menu_bar import MenuBar
from gui.nav_bar import NavigationBar
from gui.main_view import MainView
from state import AppState


root = tk.Tk()
root.title("Analysis App")
root.geometry("800x600")

state = AppState()

menu = MenuBar(root, state)        
menu.pack(side="top", fill="x")
nav = NavigationBar(root, state)
nav.pack(side="top", fill="x")
main_view = MainView(root, state)

def toggle_game():
    state.show_game = not state.show_game
    main_view.update_visibility()

root.bind("g", lambda e: toggle_game())


root.mainloop()
