from graphics import Graphics
from colors import Colors

class Enemy:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.width = 12
        self.height = 12
        self.speed = 2
        self.vx = vx
        self.vy = vy

    def Update(self):
        self.x += self.vx * self.speed
        self.y += self.vy * self.speed
        self.CheckBorders()

    def Draw(self, gfx):
        gfx.DrawRect(int(self.x), int(self.y), self.width, self.height, Colors.Red)

    def CheckBorders(self):
        if self.x <= 0:
            self.vx = -self.vx
            self.x = 0
        elif self.x + self.width >= Graphics.wndWidth:
            self.vx = -self.vx
            self.x = Graphics.wndWidth - self.width
        if self.y <= 0:
            self.vy = -self.vy
            self.y = 0
        elif self.y + self.height >= Graphics.wndHeight:
            self.vy = -self.vy
            self.y = Graphics.wndHeight - self.height