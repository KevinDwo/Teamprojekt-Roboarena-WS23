from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState
    from Game.Entities.actor import Actor

from pygame import Surface, Vector2

from Game.Entities.entity import Entity


class Bullet(Entity):
    """A bullet is an entity that can move: Can be shot by Actors."""

    def __init__(self, gameState: 'GameState', texture: Surface, position: Vector2,
                 direction: int, currentSpeed: float, maxLifetime: int, shooter: 'Actor'):
        super().__init__(gameState, texture, position, direction, currentSpeed)
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
                if type(target) is not Bullet or target.shooter != self.shooter:
                    target.hit(10)
                    self.kill()

    def hit(self, damage: int):
        super().hit(damage)
        self.kill()
