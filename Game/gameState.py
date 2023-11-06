from pygame import Vector2

from constants import windowWidth, windowHeight
from Arena.arena import Arena
from Game.robot import BasicRobot


class GameState():
    def __init__(self) -> None:
        self.worldSize = Vector2(windowWidth, windowHeight)
        self.tileSize = Vector2(32, 32)
        self.movementWidth = 5
        self.arena = Arena(self)
        self.robot = BasicRobot(self)

    def worldWidth(self):
        return self.worldSize.x

    def worldHeight(self):
        return self.worldSize.y

    def getMovementWidth(self):
        return self.movementWidth

    def update(self, movementVector, mousePosition):
        self.robot.move(movementVector)
        self.robot.rotate(mousePosition)
