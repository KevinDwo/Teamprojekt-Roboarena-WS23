from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState

from pygame import Surface, Vector2
from Game.Entities.entity import Entity


class Bullet(Entity):
    """A bullet is an entity that can move: Can be shot by robot and enemies."""

    def __init__(self, gameState: 'GameState', texture: Surface, position: Vector2,
                 direction: int, currentSpeed: float, maxLifetime: int):
        super().__init__(gameState, texture, position, direction, currentSpeed)
        self.maxLifetime = maxLifetime
        self.lifetime = 0

    def update(self):
        """Update the bullet state."""
        self.move()
        self.lifetime += 1
        if self.lifetime >= self.maxLifetime:
            self.isAlive = False
