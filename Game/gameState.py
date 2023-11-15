from pygame import Vector2, Surface
from pygame.key import ScancodeWrapper

from Game.level import decodeUnitsLayer
from constants import windowWidth, windowHeight
from Game.arena import Arena
from Game.Entities.robot import BasicRobot
import tmx


class GameState():
    def __init__(self, level: str) -> None:
        self.level = tmx.TileMap.load(f"Assets/Maps/level{level}.tmx")
        self.worldSize = Vector2(windowWidth, windowHeight)
        self.tileSize = Vector2(32, 32)
        self.arena = Arena(self, level)
        self.robots = decodeUnitsLayer(self,self.level)
        self.activeRobot = 0

    def worldWidth(self):
        return self.worldSize.x

    def worldHeight(self):
        return self.worldSize.y

    def getMovementWidth(self):
        return self.movementWidth

    def getActiveRobot(self):
        return self.robots[self.activeRobot]

    def update(self, movementVector: Vector2, direction: int):
        self.robots[self.activeRobot].move(movementVector, self.worldWidth(), self.worldHeight())
        self.robots[self.activeRobot].rotate(direction)

        self.robots = [BasicRobot(self, "Assets/player/anotherRed.png",
                                  Vector2(self.worldSize.x / 4, self.worldSize.y / 4), 1, True),
                       BasicRobot(self, "Assets/player/blue.png",
                                  Vector2(3 * self.worldSize.x / 4, self.worldSize.y / 4), 2, False),
                       BasicRobot(self, "Assets/player/deepblue.png",
                                  Vector2(self.worldSize.x / 4, 3 * self.worldSize.y / 4), 3, False),
                       BasicRobot(self, "Assets/player/gray.png",
                                  Vector2(3 * self.worldSize.x / 4, 3 * self.worldSize.y / 4), 4, False)]

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
