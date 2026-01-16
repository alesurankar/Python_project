from graphics import Graphics
from player import Player
from enemy import Enemy
import random

class App:
    def __init__(self, gfx, kbd):
        self.gfx = gfx
        self.kbd = kbd
        self.entities = []
        self.rndX = random.randint(0, Graphics.wndWidth)
        self.rndY = random.randint(0, Graphics.wndHeight)
        self.player = Player(self.rndX, self.rndY)
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

        for e in self.entities:
            if isinstance(e, Player):
                e.Update(self.kbd)
            else:
                e.Update()

    def ComposeFrame(self):
        for e in self.entities:
            e.Draw(self.gfx)