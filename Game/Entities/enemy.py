
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState
import pygame
from Game.Entities.actor import Actor


class Enemy(Actor):
    def __init__(self, gameState: 'GameState', texturePath: str, position: pygame.Vector2):
        texture = pygame.image.load(texturePath)
        direction = 0
        currentSpeed = 0
        hp = 100
        maxSpeed = 2
        acceleration = 0.05
        brakeAcceleration = 0.1
        rotationalSpeed = 3
        bulletSpeed = 5
        shootCooldown = 500
        shootRange = 200
        super().__init__(gameState, texture, position, direction, currentSpeed, maxSpeed, acceleration,
                         brakeAcceleration, rotationalSpeed, hp, bulletSpeed, shootCooldown, shootRange)
