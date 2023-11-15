from pygame import Vector2, Surface
from pygame.key import ScancodeWrapper
import tmx
from Game.level import decodeUnitsLayer

from constants import windowWidth, windowHeight
from Game.arena import Arena
from Game.Entities.robot import BasicRobot

class GameState():
    def __init__(self, level: str) -> None:
        self.level = tmx.TileMap.load(f"Assets/Maps/level{level}.tmx")
        self.worldSize = Vector2(windowWidth, windowHeight)
        self.tileSize = Vector2(32, 32)
        self.arena = Arena(self, level)
        self.robots = decodeUnitsLayer(self,self.level)
        self.entities = self.robots 

    def handleKeyPresses(self, pressed: ScancodeWrapper):
        for e in self.entities:
            e.handleKeyPresses(pressed)

    def moveEntities(self):
        for e in self.entities:
            e.move()

    def draw(self, window: Surface):
        window.fill((0, 0, 0))
        self.arena.draw(window)
        for e in self.entities:
            e.draw(window)
