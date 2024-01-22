import pygame
from pygame import Vector2, Surface
from pygame.key import ScancodeWrapper
from pygame import mixer

import tmxhandler
from Menus.panel import GameOverScreen, VictoryScreen

from constants import windowWidth, windowHeight
from Game.arena import Arena
from Game.Entities.actor import Actor


class GameState:
    def __init__(self, level: str) -> None:
        self.worldSize = Vector2(windowWidth, windowHeight)
        self.tileSize = Vector2(32, 32)
        self.arena = Arena(self, level)
        self.robots = tmxhandler.decodeRobotsLayers(self)
        self.obstacles = tmxhandler.decodeObstacleLayer(self)
        self.deadlyObstacles = tmxhandler.decodeDeadlylayer(self)
        self.enemies = tmxhandler.decodeEnemyLayer(self)
        self.entities = self.robots.copy() + self.enemies.copy()
        self.gameRunning = True
        self.animations = []

    def handleKeyPresses(self, pressed: ScancodeWrapper):
        for e in self.entities:
            e.handleKeyPresses(pressed)

    def moveEntities(self):
        if self.gameRunning:
            for e in self.entities:
                e.move()

    def draw(self, window: Surface):
        endScreen = None
        if self.gameRunning:
            window.fill((0, 0, 0))
            self.arena.drawBelowEntities(window)
            for e in self.entities:
                e.draw(window)
            for a in self.animations:
                a.draw(window)
            self.arena.drawAboveEntities(window)
            for e in self.entities:
                if isinstance(e, Actor):
                    e.drawHealthBar(window)
        elif any(x.isAlive for x in self.robots):
            if not endScreen:
                endScreen = VictoryScreen()
                pygame.mixer.music.fadeout(60)
            return endScreen.draw(window)
        else:
            if not endScreen:
                endScreen = GameOverScreen()
                pygame.mixer.music.fadeout(60)
            return endScreen.draw(window)

    def checkGameOver(self):
        if self.gameRunning:
            if not any(x for x in self.robots if x.isAlive):
                self.gameRunning = False
                mixer.Sound('Assets/Sounds/game_over2.wav').play()
            elif not any(x for x in self.enemies if x.isAlive):
                self.gameRunning = False
                mixer.Sound('Assets/Sounds/victory.wav').play()
