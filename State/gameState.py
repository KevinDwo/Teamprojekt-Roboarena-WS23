from pygame import Vector2

from Arena.arena import Arena
from Robot.robot import BasicRobot


class GameState():
    def __init__(self) -> None:
        self.worldSize = Vector2(1000, 1000)
        self.tileSize = Vector2(50, 50)
        self.movementWidth = 5
        self.arena = Arena()
        self.robot = BasicRobot()

    def worldWidth(self):
        return self.worldSize.x

    def worldHeight(self):
        return self.worldSize.y

    def getMovementWidth(self):
        return self.movementWidth

    def update(self, movementVector, mousePosition):
        self.robot.move(movementVector)
        self.robot.rotate(mousePosition)
