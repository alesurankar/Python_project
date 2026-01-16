from src.graphics import Graphics
from models.player import Player
from models.enemy import Enemy
import random

class App:
    def __init__(self, wnd):  
        self.gfx = Graphics(wnd)
        self.entities = []
        self.rndX = random.randint(0, Graphics.wndWidth)
        self.rndY = random.randint(0, Graphics.wndHeight)
        self.player = Player(self.rndX, self.rndY, wnd.kbd, wnd.mouse)
        self.entities.append(self.player)
        self.spawnRate = 0.02

    def Go(self):
        self.gfx.BeginFrame()
        self.UpdateFrame()
        self.ComposeFrame()
        self.gfx.EndFrame()

    def UpdateFrame(self):
        if random.random() < self.spawnRate:
            self.rndX = random.randint(0, Graphics.wndWidth)
            self.rndY = random.randint(0, Graphics.wndHeight)
            self.rndV = random.uniform(-2, 2)
            self.entities.append(Enemy(self.rndX, self.rndY, self.rndV, self.rndV))

        for e in self.entities[:]:
            e.Update()
            if isinstance(e, Enemy) and e.CheckCollision(self.player):
                self.entities.remove(e)

    def ComposeFrame(self):
        for e in self.entities:
            e.Draw(self.gfx)