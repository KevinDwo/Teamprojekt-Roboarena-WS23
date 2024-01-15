from typing import TYPE_CHECKING

from Animation.bulletExplosion import BulletExplosion
if TYPE_CHECKING:
    from Game.gameState import GameState
    from Game.Entities.actor import Actor

import pygame
from pygame import Vector2

from Game.Entities.entity import Entity


BulletTexture = pygame.image.load('Assets/Bullet.png')


class Bullet(Entity):
    """A bullet is an entity that can move: Can be shot by Actors."""

    def __init__(self, gameState: 'GameState', position: Vector2,
                 direction: int, currentSpeed: float, maxLifetime: int, shooter: 'Actor'):
        super().__init__(gameState, BulletTexture, position, direction, currentSpeed)
        self.maxLifetime = maxLifetime  # Maybe we can use this for later weapons
        self.initPosition = position
        self.lifetime = 0
        self.shooter = shooter

    def move(self):
        """Update the bullet state."""
        super().move(clamping=False, stuckOnCollision=True)
        self.lifetime += 1
        self.outOfBounds()
        self.checkRange()
        self.checkHit()

    def outOfBounds(self):
        if not (0 <= self.position.x <= self.gameState.worldSize.x and
                0 <= self.position.y <= self.gameState.worldSize.y):
            self.kill()

    def checkRange(self):
        if self.lifetime >= self.maxLifetime:
            self.kill()

    def checkHit(self):
        for target in self.gameState.entities:
            if target != self and target != self.shooter and self.getHitBox().colliderect(target.getHitBox()):
                # Bullets destroy each other unless shot by the same shooter - in that case, they ignore each other.
                if type(target) is Bullet and target.shooter == self.shooter:
                    return

                # No friendly fire among enemies - they are too likely to kill each other, lol
                if target in self.gameState.enemies and self.shooter in self.gameState.enemies:
                    self.kill()
                    return

                target.hit(10)
                self.kill()

    def hit(self, damage: int):
        super().hit(damage)
        self.kill()

    def kill(self, removeFromEntities=True):
        """Kills the entity: Removes it from the currently active entities"""
        if self.isAlive:
            self.isAlive = False
            self.currentSpeed = 0
            self.gameState.animations.append(BulletExplosion(self.gameState, self.position))
            if removeFromEntities:
                self.gameState.entities.remove(self)
