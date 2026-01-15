from colors import Colors


class App:
    def __init__(self, gfx, kbd):
        self.gfx = gfx
        self.kbd = kbd
        self.x = 100
        self.y = 100
        self.speed = 1

    def Go(self):
        self.gfx.BeginFrame()
        self.UpdateFrame()
        self.ComposeFrame()
        self.gfx.EndFrame()

    def UpdateFrame(self):
        if self.kbd.KeyIsPressed("K_SPACE"):
            self.speed = 3
        else: self.speed = 1
        if self.kbd.KeyIsPressed("K_w"):
            self.y -= self.speed
        if self.kbd.KeyIsPressed("K_a"):
            self.x -= self.speed
        if self.kbd.KeyIsPressed("K_s"):
            self.y += self.speed
        if self.kbd.KeyIsPressed("K_d"):
            self.x += self.speed


    def ComposeFrame(self):
        self.gfx.DrawRect(self.x, self.y, 10, 10, Colors.Red)