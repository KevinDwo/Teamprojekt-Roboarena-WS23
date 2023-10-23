import pygame


class Terrain():
    pass


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
