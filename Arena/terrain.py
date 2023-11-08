from pygame import Vector2
import pygame


class Terrain():
    pass


class Ground(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.texture = pygame.image.load('Assets/tileset x1.png')
        self.tilePosition = Vector2(34, 1)


class NorthWall(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.texture = pygame.image.load('Assets/tileset x1.png')
        self.tilePosition = Vector2(5, 0)


class SouthWall(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.texture = pygame.image.load('Assets/tileset x1.png')
        self.tilePosition = Vector2(5, 10)


class EastWall(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.texture = pygame.image.load('Assets/tileset x1.png')
        self.tilePosition = Vector2(9, 2)


class WestWall(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.texture = pygame.image.load('Assets/tileset x1.png')
        self.tilePosition = Vector2(1, 2)


class Acid(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.texture = pygame.image.load('Assets/tileset x1.png')
        self.tilePosition = Vector2(36, 3)


class Default(Terrain):
    def __init__(self) -> None:
        self.texture = pygame.image.load('Assets/tileset x1.png')
        self.tilePosition = Vector2(1, 35)
