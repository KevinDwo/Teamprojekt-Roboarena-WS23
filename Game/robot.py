from pygame import Vector2, Surface
import pygame
import math


class BasicRobot():
    '''The BasicRobot class represents a playable basic robot
with a position, radius and direction.'''
    def __init__(self, gameState, x, y, image) -> None:
        self.gameState = gameState
        self.cellSize = gameState.tileSize
        self.position = Vector2(x, y)  # Position in coordinates
        self.radius = 25  # Radius in pixels
        self.direction = 0  # Angle of orientation, direction ∊ (-180, 180]
        self.image = pygame.image.load(image)  # RGB color of the robot

    def move(self,
             movementVector: Vector2,
             windowWidth: int,
             windowHeight: int):
        """Moves the robot by `movementVector`
        in the given window boundaries"""
        self.position += movementVector
        self.position.x = clamp(self.position.x,
                                self.radius,
                                windowWidth - self.radius)
        self.position.y = clamp(self.position.y,
                                self.radius,
                                windowHeight - self.radius)

    def rotate(self, mousePosition: Vector2):
        """Rotates the robot towards `mousePosition`"""
        self.direction = (mousePosition - self.position).as_polar()[1]

    def draw(self, surface: Surface, selected: bool):
        """Draws the robot on the `surface`"""
        spritePoint = self.position
        texturePoint = Vector2(0, 0).elementwise()*self.cellSize
        textureRect = pygame.Rect(int(texturePoint.x), int(texturePoint.y), int(self.cellSize.x),int(self.cellSize.y))
        image = self.image.subsurface(textureRect)
        if self.direction == 0:
            surface.blit(image, spritePoint)
        else:
            rotatedImage = pygame.transform.rotate(image, -self.direction)
            spritePoint.x += (image.get_width() - image.get_width()) // 2
            spritePoint.y -= (image.get_height() - image.get_height()) // 2
            surface.blit(rotatedImage, spritePoint)
        if selected:
            pygame.draw.circle(surface, 'red', self.position, 2, 5)

        """ lineVector = Vector2.from_polar((self.radius, self.direction))
        pygame.draw.line(surface,
                        (0, 0, 0),
                        self.position,
                        self.position + lineVector) """


def clamp(x: int, minimum: int, maximum: int) -> int:
    """Returns x if x ∊ [minimum, maximum],
    otherwise minimum if x is smaller and maximum
    if x is larger than that."""
    return min(max(x, minimum), maximum)
