from pygame import Vector2
import pygame

#definition of windowsize aufgrund fehlendes game state
windowWidth = 1000
windowHeight = 1000

#robot class that defines a new player
class Robot():
    def __init__(self) -> None:
        self.position = Vector2(500,500)
        self.radius = 25
        self.direction = Vector2(self.position.x,self.position.y + self.radius)
        self.color = (0,0,255)
        self.line = (self.position, Vector2(self.position,self.position.y + self.radius / 2))
    
    # defines movement of robot
    def move(self, movementVector: Vector2):
        self.position += movementVector
        self.direction += movementVector
        self.position.x = clamp(self.position.x, 0, windowWidth - self.radius)
        self.position.y = clamp(self.position.y, 0, windowHeight - self.radius)
    
    #defines rotation 
    def rotate(self, rotation: Vector2):
        self.direction = rotation
    
    #draws robot    
    def draw(self, surface):
        pygame.draw.circle(surface, self.color , self.position , self.radius)
        pygame.draw.line(surface, (0,0,0), self.position, self.direction)


def clamp(x: int, minimum: int, maximum: int) -> int:
    """Returns x if x ∊ [minimum, maximum], otherwise minimum if x is smaller and maximum if x is larger than that."""
    return min(max(x, minimum), maximum)