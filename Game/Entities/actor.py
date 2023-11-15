from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState

from pygame import Vector2, Surface

from Game.Entities.entity import Entity


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
