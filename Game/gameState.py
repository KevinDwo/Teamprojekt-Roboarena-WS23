from pygame import Vector2, Surface
from pygame.key import ScancodeWrapper
import tmx

from Game.level import decodeDeadlylayer, decodeObstacleLayer, decodeUnitsLayer, decodeEnemyLayer
from Menus.Panel import GameOverScreen
from constants import windowWidth, windowHeight
from Game.arena import Arena


class GameState:
    def __init__(self, level: str) -> None:
        self.level = tmx.TileMap.load(f"Assets/Maps/level{level}.tmx")
        self.worldSize = Vector2(windowWidth, windowHeight)
        self.tileSize = Vector2(32, 32)
        self.arena = Arena(self, level)
        self.robots = decodeUnitsLayer(self, self.level)
        self.obstacles = decodeObstacleLayer(self.level)
        self.deadlyObstacles = decodeDeadlylayer(self.level)
        self.Enemies = decodeEnemyLayer(self, self.level)
        self.entities = self.robots.copy() + self.Enemies.copy()
        self.gameRunning = True

    def handleKeyPresses(self, pressed: ScancodeWrapper):
        for e in self.entities:
            e.handleKeyPresses(pressed)

    def moveEntities(self):
        for e in self.entities:
            e.move()

    def draw(self, window: Surface):
        if self.gameRunning:
            window.fill((0, 0, 0))
            self.arena.drawBelowEntities(window)
            for e in self.entities:
                e.draw(window)
            self.arena.drawAboveEntities(window)
            for e in self.entities:
                e.drawHealthBar(window)
        else:
            gameOverScreen = GameOverScreen()
            gameOverScreen.draw(window)

    def checkGameOver(self):
        if not any(x for x in self.robots if x.isAlive):
            self.gameRunning = False
