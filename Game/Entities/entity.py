from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState

from pygame import Surface, Vector2
from pygame.key import ScancodeWrapper

from utils import clamp, degreesToUnitVector


# Entity is an Abstract Base Class (ABC), that requires subclasses to provide implementations for abstract methods.
class Entity(ABC):
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

    width: int
    """Width of the entity (for its hitbox)"""

    height: int
    """Height of the entity (for its hitbox)"""

    def __init__(self, gameState: 'GameState', texture: Surface, position: Vector2, direction: Vector2, currentSpeed: int):
        self.gameState = gameState
        self.isAlive = True
        self.texture = texture
        self.position = position
        self.direction = direction
        self.currentSpeed = currentSpeed
        self.width = texture.get_width()
        self.height = texture.get_height()

    @abstractmethod
    def draw(self, surface: Surface):
        """Draws the entity to the screen. This method must be overridden by subclasses!"""

    def move(self):
        """Moves the entity based on its current direction and speed"""
        movementVector = self.currentSpeed * degreesToUnitVector(self.direction)
        newPosition = self.position + movementVector
        newPosition.x = clamp(newPosition.x, 0, self.gameState.worldSize.x - self.texture.get_width())
        newPosition.y = clamp(newPosition.y, 0, self.gameState.worldSize.y - self.texture.get_height())
        self.position = newPosition

    def rotate(self, rotateBy: int):
        """Rotates the entity by rotateBy degrees"""
        self.direction = (self.direction + rotateBy) % 360

    def handleKeyPresses(self, pressed: ScancodeWrapper):
        """This method can be overridden by subclasses to handle keys that are pressed down"""
