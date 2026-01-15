import pygame
from colors import Colors


class Graphics:
    def __init__(self, window):
        self.window = window
        self.screen = window.screen        
        self.width = window.width
        self.height = window.height
        self.clock = window.clock

    def PutPixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            if hasattr(color, "r"):
                self.screen.set_at((x, y), (color.r, color.g, color.b))
            else:
                self.screen.set_at((x, y), color)

    def DrawRect(self, x, y, width, height, color):
        for iy in range(y, y + height):
            for ix in range(x, x + width):
                self.PutPixel(ix, iy, color)


    def BeginFrame(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def EndFrame(self):
        pygame.display.flip()
        self.clock.tick(60)
