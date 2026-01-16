from livingEntity import LivingEntity
from colors import Colors

class Enemy(LivingEntity):
    def __init__(self, x, y, vx, vy):
        super().__init__(x, y, vx, vy, Colors.Red)

    def Update(self):
        super().Update()
        super().CheckBorders()

    def Draw(self, gfx):
        super().Draw(gfx)