from pygame import Vector2

from Arena.arena import Arena
from Robot.robot import Robot


class GameState():
    def __init__(self) -> None:
        self.worldSize = Vector2(1000,1000)
        self.tileSize = Vector2(50,50)
        self.movementWidth = 5
        self.arena = Arena()
        self.robot = Robot(self)
        
    def worldWidth(self):
        return self.worldSize.x
    
    def worldHeight(self):
        return self.worldSize.y
    
    def update(self, movementVector, mousePosition):
        self.robot.move(movementVector)
        self.robot.rotate(mousePosition)
    