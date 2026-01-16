from graphics import Graphics

class LivingEntity:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.width = 12
        self.height = 12

    def Update(self):
        self.x += self.vx
        self.y += self.vy

    def Draw(self, gfx):
        gfx.DrawRect(int(self.x), int(self.y), self.width, self.height, self.color)

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