from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState
import random

import pygame
from pygame import Surface

from constants import enemyChooseNewTargetChance, enemyShootChance
from utils import isRightOf
from Game.Entities.actor import Actor


class Enemy(Actor):
    def __init__(self, gameState: 'GameState', texture: Surface, position: pygame.Vector2):
        direction = 0
        currentSpeed = 0
        hp = 50
        maxSpeed = 2
        acceleration = 0.05
        brakeAcceleration = 0.015
        rotationalSpeed = 1.5
        bulletSpeed = 3
        shootCooldown = 500
        shootRange = 200
        super().__init__(gameState, texture, position, direction, currentSpeed, maxSpeed, acceleration,
                         brakeAcceleration, rotationalSpeed, hp, bulletSpeed, shootCooldown, shootRange)
        self.target = None
        self.currentChosenDirection = 0
        self.lastChoosePosition = None
        self.lastChooseTime = 1000

    def move(self):
        super().move()
        if self.isAlive:
            self.chooseTarget()
            if not self.target:
                self.brake()
                return

            self.chooseDirection()
            if abs(self.direction - self.currentChosenDirection) >= 2 * self.rotationalSpeed:
                self.brake()
                if isRightOf(self.direction, self.currentChosenDirection):
                    self.rotateLeft()
                else:
                    self.rotateRight()
            elif (self.position - self.target.position).length() >= 100:
                self.accelerate()
            else:
                self.brake()

            if random.randint(0, 99) < enemyShootChance:
                self.shoot()

    def kill(self):
        super().kill(False)
        self.gameState.checkGameOver()

    def chooseTarget(self):
        if (not self.target) or (random.randint(0, 999) / 10 < enemyChooseNewTargetChance):
            targets = [x for x in self.gameState.robots if x.isAlive]
            targets.sort(key=lambda x: (x.position - self.position).length())
            if not targets:
                return
            self.target = targets[0]

    def chooseDirection(self):
        self.lastChooseTime += 1
        if self.lastChooseTime > random.randint(30, 60):
            self.lastChooseTime = 0

            baseDirection = 0
            if self.target:
                baseDirection = pygame.Vector2.angle_to(pygame.Vector2(0, 0), self.target.position - self.position) % 360

            if self.lastChoosePosition and (self.position - self.lastChoosePosition).length() < 1 and self.currentSpeed > 0:
                # enemy is not moving despite trying to move - it's stuck in a wall. Try rotating by 90 degrees.
                if random.randint(0, 1) == 0:
                    baseDirection = (baseDirection + 90) % 360
                else:
                    baseDirection = (baseDirection - 90) % 360
                self.lastChooseTime = -150
                self.lastChoosePosition = None
            else:
                self.lastChoosePosition = self.position.copy()

            self.currentChosenDirection = baseDirection
