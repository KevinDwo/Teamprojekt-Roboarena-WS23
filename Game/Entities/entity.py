from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState

import pygame
from pygame import Surface, Vector2, Rect
from pygame.key import ScancodeWrapper

from utils import degreesToUnitVector


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
                 currentSpeed: float):
        self.gameState = gameState
        self.isAlive = True
        self.texture = texture
        self.position = position
        self.direction = direction
        self.currentSpeed = currentSpeed
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

    def move(self, stuckOnCollision=False):
        """Moves the entity based on its current direction and speed"""
        if self.isAlive:
            movementVector = self.currentSpeed * degreesToUnitVector(self.direction)

            newHitBox = self.getHitBox()
            newPositions = [self.position + movementVector,   # both horiz. and vert. free, this is where the robot wants to go
                            self.position + Vector2(movementVector.x, 0),  # if vert. blocked, try to go horiz. by x-component
                            self.position + Vector2(0, movementVector.y)]  # if horiz. blocked, try to go vert. by y-component

            for newPosition in newPositions:
                newHitBox.center = newPosition + (self.size / 2)

                for obstacle in self.gameState.obstacles:
                    if newHitBox.colliderect(obstacle):  # Can't move to that position
                        if stuckOnCollision:             # Either: Get stuck at this place and stop moving
                            self.currentSpeed = 0
                            return
                        break                            # Or: Try the other positions - sliding along the wall horiz. or vert.
                else:  # No obstacle collided at that newPosition
                    self.position = newPosition
                    return

    def rotate(self, rotateBy: int):
        """Rotates the entity by rotateBy degrees"""
        if self.isAlive:
            self.direction = (self.direction + rotateBy) % 360

    def kill(self, removeFromEntities=True):
        """Kills the entity: Removes it from the currently active entities"""
        if self.isAlive:
            self.isAlive = False
            self.currentSpeed = 0
            if removeFromEntities:
                self.gameState.entities.remove(self)

    def handleKeyPresses(self, pressed: ScancodeWrapper):
        """This method can be overridden by subclasses to handle keys that are pressed down"""

    def hit(self, strength: int):
        """Occurs when the entity takes damage. Can be overriden by subclasses."""
