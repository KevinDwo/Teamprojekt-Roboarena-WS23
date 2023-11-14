import math

from pygame import Vector2, Surface
import pygame


class BasicRobot:
    '''The BasicRobot class represents a playable basic robot
       with a position, radius and direction.'''

    def __init__(self, gameState, x, y, image) -> None:
        self.gameState = gameState
        self.cellSize = gameState.tileSize
        self.position = Vector2(x, y)  # Position in coordinates
        self.direction = 0  # Angle of orientation, direction ∊ [0, 360)
        self.texture = pygame.image.load(image)  # RGB color of the robot

    def move(self,
             movementVector: Vector2,
             windowWidth: int,
             windowHeight: int):
        """Moves the robot by `movementVector`
        in the given window boundaries"""
        self.position += movementVector
        self.position.x = clamp(self.position.x,
                                0,
                                windowWidth - self.cellSize.x)
        self.position.y = clamp(self.position.y,
                                0,
                                windowHeight - self.cellSize.y)

    def rotate(self, newDirection):
        """Rotates the robot according to rotationalSpeed"""
        self.direction = (self.direction + newDirection) % 360

    def computeMovement(self):
        return Vector2(math.cos(math.radians(self.direction)),
                       math.sin(math.radians(self.direction)))

    def draw(self, surface: Surface, selected: bool):
        """Draws the robot on the `surface`"""
        texturePoint = Vector2(0, 0).elementwise()*self.cellSize
        textureRect = pygame.Rect(int(texturePoint.x),
                                  int(texturePoint.y),
                                  int(self.cellSize.x),
                                  int(self.cellSize.y))
        textureTile = pygame.Surface(self.cellSize, pygame.SRCALPHA)
        textureTile.blit(self.texture, (0, 0), textureRect)
        rect = textureTile.get_rect()
        rect.center = self.position + (self.cellSize / 2)
        rotatedImage = pygame.transform.rotate(textureTile, -self.direction)
        rotatedRect = rotatedImage.get_rect()
        rotatedRect.center = rect.center
        surface.blit(rotatedImage, rotatedRect)
        if selected:
            pygame.draw.circle(surface, 'red', self.position, 2, 5)


def clamp(x: int, minimum: int, maximum: int) -> int:
    """Returns x if x ∊ [minimum, maximum],
    otherwise minimum if x is smaller and maximum
    if x is larger than that."""
    return min(max(x, minimum), maximum)
