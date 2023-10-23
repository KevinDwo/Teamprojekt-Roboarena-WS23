from pygame import Vector2
import pygame


class Terrain():
    def __init__(self) -> None:
        self.size = Vector2(50, 50)


class Grass(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.color = pygame.Color('#8BC34A')


class Stone(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.color = pygame.Color('#9E9E9E')


class Water(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.color = pygame.Color('#1976D2')


class Mud(Terrain):
    def __init__(self) -> None:
        super().__init__()
        self.color = pygame.Color('#795548')
