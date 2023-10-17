from pygame import Vector2
import pygame

<<<<<<< HEAD
=======
#definition of windowsize aufgrund fehlendes game state
windowWidth = 1000
windowHeight = 1000
>>>>>>> c01c7c3 (added an arena class to store the field)

# The BasicRobot class represents a playable basic robot
# with a position, radius and direction.
class BasicRobot():
    def __init__(self) -> None:
<<<<<<< HEAD
        self.position = Vector2(500, 500)  # Position in coordinates
        self.radius = 25  # Radius in pixels
        self.direction = 0  # Angle of orientation in degrees, direction ∊ (-180, 180]
        self.color = (0, 0, 255)  # RGB color of the robot

    def move(self, movementVector: Vector2, windowWidth: int, windowHeight: int):
        """Moves the robot by `movementVector` in the given window boundaries"""
=======
        self.position = Vector2(500,500)
        self.radius = 25
        self.direction = Vector2(self.position.x,self.position.y + self.radius)
        self.color = (0,0,255)
        self.line = (self.position, Vector2(self.position,self.position.y + self.radius / 2))
    
    # defines movement of robot
    def move(self, movementVector: Vector2):
>>>>>>> c01c7c3 (added an arena class to store the field)
        self.position += movementVector
        self.position.x = clamp(self.position.x, 0, windowWidth - self.radius)
        self.position.y = clamp(self.position.y, 0, windowHeight - self.radius)

    def rotate(self, mousePosition: Vector2):
        """Rotates the robot towards `mousePosition`"""
        self.direction = (mousePosition - self.position).as_polar()[1]

    def draw(self, surface):
        """Draws the robot on the `surface`"""
        pygame.draw.circle(surface, self.color, self.position, self.radius)

        lineVector = Vector2.from_polar((self.radius, self.direction))
        pygame.draw.line(surface,
                         (0, 0, 0),
                         self.position,
                         self.position + lineVector)


def clamp(x: int, minimum: int, maximum: int) -> int:
    """Returns x if x ∊ [minimum, maximum],
    otherwise minimum if x is smaller and maximum
    if x is larger than that."""
    return min(max(x, minimum), maximum)
