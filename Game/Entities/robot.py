from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from Game.gameState import GameState

from pygame import Vector2, Surface
from pygame.key import ScancodeWrapper
import pygame

from Game.Entities.actor import Actor


class BasicRobot(Actor):
    """The BasicRobot class represents a playable basic robot with a position, radius and direction."""

    number: int
    """The number identifier (1, 2, ...) of this robot"""

    selected: bool
    """Indicates whether this robot is currently selected to play with"""

    def __init__(self, gameState: 'GameState', texturePath: str, position: Vector2, number: int, selected: bool):
        texture = pygame.image.load(texturePath)
        direction = 0
        currentSpeed = 0
        hp = 100
        maxSpeed = 2
        acceleration = 0.05
        brakeAcceleration = 0.1
        rotationalSpeed = 3
        super().__init__(gameState, texture, position, direction, currentSpeed, maxSpeed,
                         acceleration, brakeAcceleration, rotationalSpeed, hp)
        self.number = number
        self.selected = selected

    def draw(self, surface: Surface):
        """Draws the robot on the `surface`"""
        super().draw(surface)
        if self.selected:
            pygame.draw.circle(surface, 'red', self.position, 2, 5)

    def updateSelected(self, pressed: ScancodeWrapper):
        keys = {1: pygame.K_1, 2: pygame.K_2, 3: pygame.K_3, 4: pygame.K_4}

        # This robot is being selected,
        # but if multiple selection keys are pressed, select only the one with the smallest number
        if pressed[keys[self.number]] and not any(pressed[keys[x]] for x in keys if x < self.number):
            self.selected = True

        # Another robot is being selected, unselect this one
        elif any(pressed[keys[x]] for x in keys if x != self.number):
            self.selected = False

    def updateMovement(self, pressed: ScancodeWrapper):
        if not self.selected:
            return

        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.rotateRight()
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self.rotateLeft()
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self.brake()
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            self.accelerate()

    def handleKeyPresses(self, pressed: ScancodeWrapper):
        self.updateSelected(pressed)
        self.updateMovement(pressed)
