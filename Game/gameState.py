from pygame import Vector2, Surface
from pygame.key import ScancodeWrapper

from constants import windowWidth, windowHeight
from Game.arena import Arena
from Game.Entities.robot import BasicRobot


class GameState():
    def __init__(self, level: str) -> None:
        self.level = level
        self.worldSize = Vector2(windowWidth, windowHeight)
        self.tileSize = Vector2(32, 32)
        self.arena = Arena(self, level)

        self.robots = [BasicRobot(self, "Assets/player/anotherRed.png",
                                  Vector2(self.worldSize.x / 4, self.worldSize.y / 4), 1),
                       BasicRobot(self, "Assets/player/blue.png",
                                  Vector2(3 * self.worldSize.x / 4, self.worldSize.y / 4), 2)]

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
