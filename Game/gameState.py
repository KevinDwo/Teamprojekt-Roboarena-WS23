from pygame import Vector2

from constants import windowWidth, windowHeight
from Game.arena import Arena
from Game.robot import BasicRobot


class GameState:
    def __init__(self) -> None:
        self.worldSize = Vector2(windowWidth, windowHeight)
        self.tileSize = Vector2(50, 50)
        self.movementWidth = 5
        self.arena = Arena(self)

        self.robots = [BasicRobot(self, windowWidth / 4, windowHeight / 4, 'cyan'),
                       BasicRobot(self, 3 * windowWidth / 4, windowHeight / 4, 'yellow'),
                       BasicRobot(self, windowWidth / 4, 3 * windowHeight / 4, 'gray50'),
                       BasicRobot(self, 3 * windowWidth / 4, 3 * windowHeight / 4, 'indianred')]
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

    def draw(self, window):
        window.fill((0, 0, 0))
        self.arena.draw(window)
        for i in range(len(self.robots)):
            robot = self.robots[i]
            selected = i == self.activeRobot
            robot.draw(window, selected)

    def selectRobot(self, robotNo: int):
        self.activeRobot = robotNo
