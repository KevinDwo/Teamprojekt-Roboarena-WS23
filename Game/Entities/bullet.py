from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Game.gameState import GameState

from pygame import Surface, Vector2
from Game.Entities.entity import Entity


class Bullet(Entity):
    """A bullet is an entity that can move: Can be shot by Actors."""

    def __init__(self, gameState: 'GameState', texture: Surface, position: Vector2,
                 direction: int, currentSpeed: float, maxLifetime: int):
        super().__init__(gameState, texture, position, direction, currentSpeed)
        self.maxLifetime = maxLifetime  # Maybe we can use this for later weapons
        self.lifetime = 0

    def move(self):
        """Update the bullet state."""
        super().move(clamping=False)
        self.lifetime += 1
        self.outOfBounds()
        self.checkRange()

    def outOfBounds(self):
        if not (0 <= self.position.x <= self.gameState.worldSize.x and
                0 <= self.position.y <= self.gameState.worldSize.y):
            self.kill()

    def checkRange(self):
        if self.lifetime >= self.maxLifetime:
            self.kill()
