from constants import windowHeight, windowWidth
import pygame
from pygame import Surface, Vector2
from typing import Tuple


class Button:
    def __init__(self, pos: Vector2, width: int = 1, height: int = 1, text: str = '', onClick=None):
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.texture = pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonNormal.png'),
                                              (width, height))
        self.onClick = onClick

    def draw(self, window: Surface):
        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(self.texture, (self.pos.x, self.pos.y, self.width, self.height))
        window.blit(text,
                    (self.pos.x + (self.width/2 - text.get_width()/2),
                     self.pos.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos: Tuple[int, int]) -> bool:
        return self.pos.x <= pos[0] <= self.pos.x + self.width and \
               self.pos.y <= pos[1] <= self.pos.y + self.height

    def setState(self, state: str):
        pass


class MenuButton(Button):
    def __init__(self, pos: Vector2, text: str = '', onClick=None):
        super().__init__(pos, 0, 0, text, onClick)
        self.height = windowHeight / 10
        self.width = windowWidth / 2
        self.states = {
            'normal': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonNormal.png'),
                                             (self.width, self.height)),
            'hover': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonHover.png'),
                                            (self.width, self.height)),
            'pressed': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonActive.png'),
                                              (self.width, self.height))
        }

    def setState(self, state: str):
        self.texture = self.states[state]


class LevelButton(Button):
    def __init__(self, pos: Vector2, text: str = '', onClick=None):
        super().__init__(pos, 0, 0, text, onClick)
        self.height = 70
        self.width = 70
        self.states = {
            'normal': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/LevelButtonNormal.png'),
                                             (self.width, self.height)),
            'hover': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/LevelButtonHover.png'),
                                            (self.width, self.height))
        }

    def setState(self, state: str):
        self.texture = self.states[state]
