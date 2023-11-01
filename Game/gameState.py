from pygame import Vector2

from constants import windowWidth, windowHeight
from Game.arena import Arena
from Game.robot import BasicRobot


class GameState():
    def __init__(self) -> None:
        self.worldSize = Vector2(windowWidth, windowHeight)
        self.tileSize = Vector2(50, 50)
        self.movementWidth = 5
        self.arena = Arena(self)
        self.robot = BasicRobot(self)

    def worldWidth(self):
        return self.worldSize.x

    def worldHeight(self):
        return self.worldSize.y

    def getMovementWidth(self):
        return self.movementWidth

    def update(self, movementVector: Vector2, mousePosition: Vector2):
        self.robot.move(movementVector, self.worldWidth(), self.worldHeight())
        self.robot.rotate(mousePosition)

    def draw(self, window):
        window.fill((0, 0, 0))
        self.arena.draw(window)
        self.robot.draw(window)
