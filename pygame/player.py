from livingEntity import LivingEntity
from graphics import Graphics
from colors import Colors

class Player(LivingEntity):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, Colors.Green)
        self.speed = 1

    def Update(self, kbd):
        if kbd.KeyIsPressed("K_SPACE"):
            self.speed = 3
        else: self.speed = 1
        if kbd.KeyIsPressed("K_w"):
            self.vy = -self.speed
        if kbd.KeyIsPressed("K_a"):
            self.vx = -self.speed
        if kbd.KeyIsPressed("K_s"):
            self.vy = self.speed
        if kbd.KeyIsPressed("K_d"):
            self.vx = self.speed
        super().Update()
        super().CheckBorders()

    def Draw(self, gfx):
        super().Draw(gfx)