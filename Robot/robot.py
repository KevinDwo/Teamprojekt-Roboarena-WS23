from pygame import Vector2
import pygame


# The BasicRobot class represents a playable basic robot with a position, radius and direction.
class BasicRobot():
    def __init__(self) -> None:
        self.position = Vector2(320, 240)
        self.radius = 40
        self.direction = Vector2(self.position.x, self.position.y + self.radius)
        self.color = (0, 0, 255)
        self.line = (self.position, Vector2(self.position, self.position.y + self.radius / 2))

    def move(self, movementVector: Vector2, windowWidth: int, windowHeight: int):
        """Moves the robot by `movementVector` in the given window boundaries"""
        self.position += movementVector
        self.direction += movementVector
        self.position.x = clamp(self.position.x, 0, windowWidth - self.radius)
        self.position.y = clamp(self.position.y, 0, windowHeight - self.radius)

    def rotate(self, mousePosition: Vector2):
        """Rotates the robot towards `mousePosition`"""
        differenceVector = mousePosition - self.position
        norm = differenceVector.normalize()
        self.direction = self.position + norm * self.radius

    def draw(self, surface):
        """Draws the robot on the `surface`"""
        pygame.draw.circle(surface, self.color, self.position, self.radius)
        pygame.draw.line(surface, (0, 0, 0), self.position, self.direction)


def clamp(x: int, minimum: int, maximum: int) -> int:
    """Returns x if x ∊ [minimum, maximum], otherwise minimum if x is smaller and maximum if x is larger than that."""
    return min(max(x, minimum), maximum)
