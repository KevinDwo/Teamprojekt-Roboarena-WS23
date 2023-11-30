from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState

import pygame
from pygame import Surface, Vector2, Rect
from pygame.key import ScancodeWrapper

from utils import clamp, degreesToUnitVector


class Entity:
    """Interface for all entities that can move on the screen"""

    isAlive: bool
    """Indicates if the entity is currently alive and active"""

    texture: Surface
    """The graphical texture of the entity"""

    position: Vector2
    """Current position of the entity on the map"""

    direction: float
    """Angle in degrees indicating the direction in which the entity is facing"""

    currentSpeed: float
    """Indicates by how much the entity moves per frame (velocity)"""

    size: Vector2
    """Size (width = x, height = y) of the entity"""

    def __init__(self, gameState: 'GameState', texture: Surface,
                 position: Vector2, direction: float,
                 currentSpeed: float, hasHealth: (bool, int)):
        self.gameState = gameState
        self.isAlive = True
        self.texture = texture
        self.position = position
        self.direction = direction
        self.currentSpeed = currentSpeed
        self.hasHealth = hasHealth
        self.size = Vector2(texture.get_size())

    def getHitBox(self) -> Rect:
        """Gets the rectangular hitbox of the entity. Can be overridden, defaults to the rect of its texture."""
        hb = self.texture.get_rect()
        hb.center = self.position + (self.size / 2)
        return hb

    def draw(self, surface: Surface):
        """Draws the entity to the screen."""
        rotatedImage = pygame.transform.rotate(self.texture, -self.direction)
        rotatedRect = rotatedImage.get_rect()
        rotatedRect.center = self.position + (self.size / 2)
        surface.blit(rotatedImage, rotatedRect)
        if (self.hasHealth[0]):
            healthbar = pygame.Surface((self.hasHealth[1] / 2, 2))
            surface.blit(healthbar, healthbar.fill((50, 205, 50)).clamp(rotatedRect))

    def move(self, clamping=True):
        """Moves the entity based on its current direction and speed"""
        if self.isAlive:
            movementVector = self.currentSpeed * degreesToUnitVector(self.direction)
            newPosition = self.position + movementVector

            newHitBox = self.getHitBox().copy()
            newHitBox.center = newPosition + (self.size / 2)

            if clamping:
                newPosition.x = clamp(newPosition.x, 0, self.gameState.worldSize.x - self.size.x)
                newPosition.y = clamp(newPosition.y, 0, self.gameState.worldSize.y - self.size.y)

            for obstacle in self.gameState.obstacles:
                if newHitBox.colliderect(obstacle):  # Can't move to new position - get stuck and lose all speed.
                    self.currentSpeed = 0
                    return

            self.position = newPosition

    def rotate(self, rotateBy: int):
        """Rotates the entity by rotateBy degrees"""
        if self.isAlive:
            self.direction = (self.direction + rotateBy) % 360

    def kill(self, removeFromEntities=True):
        """Kills the entity: Removes it from the currently active entities"""
        self.isAlive = False
        self.currentSpeed = 0
        self.hasHealth = (False, 0)
        if removeFromEntities:
            self.gameState.entities.remove(self)

    def handleKeyPresses(self, pressed: ScancodeWrapper):
        """This method can be overridden by subclasses to handle keys that are pressed down"""

    def updateHp(self, health):
        self.hasHealth = health
