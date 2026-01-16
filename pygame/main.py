from src.window import Window
from src.app import App

scrWidth = 800
scrHeight = 600
FPS = 60

wnd = Window(scrWidth, scrHeight, FPS)
app = App(wnd)

while wnd.ProcessMessage():
    app.Go()

wnd.Quit()