from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState

from pygame import Vector2, Surface

from Game.Entities.entity import Entity

import pygame

from Game.Entities.bullet import Bullet
from utils import degreesToUnitVector


class Actor(Entity):
    """An actor is an entity that can actively move, shoot, etc: A robot or an enemy."""

    maxSpeed: float
    """Maximum possible velocity"""

    acceleration: float
    """How much the velocity increases when initiating movement"""

    brakeAcceleration: float
    """How much the velocity decreases when braking"""

    rotationalSpeed: float
    """How many degrees the robot can turn per frame"""

    hp: int
    """Current amount of health points"""

    maxHp: int
    """Maximum possible amount of health points"""

    def __init__(self, gameState: 'GameState', texture: Surface, position: Vector2,
                 direction: Vector2, currentSpeed: float, maxSpeed: float, acceleration: float,
                 brakeAcceleration: float, rotationalSpeed: float, hp: int):
        super().__init__(gameState, texture, position, direction, currentSpeed)
        self.maxSpeed = maxSpeed
        self.acceleration = acceleration
        self.brakeAcceleration = brakeAcceleration
        self.rotationalSpeed = rotationalSpeed
        self.hp = hp
        self.maxHp = hp

    def accelerate(self):
        self.currentSpeed = min(self.currentSpeed + self.acceleration, self.maxSpeed)

    def brake(self):
        self.currentSpeed = max(self.currentSpeed - self.brakeAcceleration, 0)

    def rotateRight(self):
        self.rotate(self.rotationalSpeed)

    def rotateLeft(self):
        self.rotate(-self.rotationalSpeed)

    def shoot(self):
        """Create and return a bullet entity based on the current state of the actor."""
        bulletTexture = pygame.Surface((5, 5))  # Adjust the size of the bullet
        bulletTexture.fill((255, 0, 0))  # Red color for the bullet, you can change it
        bulletPosition = self.position + (self.size / 2)
        bulletDirection = self.direction
        bulletSpeed = 5  # Adjust the speed of the bullet
        return Bullet(self.gameState, bulletTexture, bulletPosition, bulletDirection, bulletSpeed, maxLifetime=60)
