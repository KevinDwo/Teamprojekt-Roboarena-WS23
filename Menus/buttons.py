from typing import Tuple, Dict

import pygame
from pygame import Surface, Vector2

from constants import windowHeight, windowWidth


class Button:
    def __init__(self, pos: Vector2, width: int, height: int, textures: Dict, initialState: str,
                 text: str = '', fontSize: int = 60, onClick=None):
        self.pos = pos
        self.width = width
        self.height = height
        self.textures = textures
        self.state = initialState
        self.onClick = onClick
        self.renderedText = None

        if text:
            font = pygame.font.SysFont('arial', fontSize)
            self.renderedText = font.render(text, 1, (255, 255, 255))

    def draw(self, window: Surface):
        window.blit(self.textures[self.state], (self.pos.x, self.pos.y, self.width, self.height))
        if self.renderedText:
            window.blit(self.renderedText,
                        (self.pos.x + (self.width/2 - self.renderedText.get_width()/2),
                         self.pos.y + (self.height/2 - self.renderedText.get_height()/2)))

    def isOver(self, pos: Tuple[int, int]) -> bool:
        return self.pos.x <= pos[0] <= self.pos.x + self.width and \
               self.pos.y <= pos[1] <= self.pos.y + self.height


class MenuButton(Button):
    def __init__(self, pos: Vector2, text: str = '', fontSize: int = 60, onClick=None):
        width = windowWidth / 2
        height = windowHeight / 10
        textures = {
            'normal': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonNormal.png'),
                                             (width, height)),
            'hover': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonHover.png'),
                                            (width, height)),
            'pressed': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonActive.png'),
                                              (width, height))
        }
        super().__init__(pos, width, height, textures, 'normal', text, fontSize, onClick)


class GameEndButton(Button):
    def __init__(self, pos: Vector2, text: str = '', fontSize: int = 60, onClick=None):
        width = windowWidth / 3
        height = windowHeight / 10
        textures = {
            'normal': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonNormal.png'),
                                             (width, height)),
            'hover': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonHover.png'),
                                            (width, height)),
            'pressed': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonActive.png'),
                                              (width, height))
        }
        super().__init__(pos, width, height, textures, 'normal', text, fontSize, onClick)


class LevelButton(Button):
    def __init__(self, pos: Vector2, text: str = '', fontSize: int = 60, onClick=None):
        width = 70
        height = 70
        textures = {
            'normal': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/LevelButtonNormal.png'),
                                             (width, height)),
            'hover': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/LevelButtonHover.png'),
                                            (width, height))
        }
        super().__init__(pos, width, height, textures, 'normal', text, fontSize, onClick)


class PlayerSelectionButton(Button):
    def __init__(self, pos: Vector2, onClick=None):
        width = windowWidth / 5
        height = windowHeight / 10
        self.selected = False
        textures = {
            'normal': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonNormal.png'),
                                             (width, height)),
            'hover': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonHover.png'),
                                            (width, height)),
            'pressed': pygame.transform.scale(pygame.image.load('Assets/Menu/Buttons/MenuButtonActive.png'),
                                              (width, height))
        }
        super().__init__(pos, width, height, textures, 'normal', 'Select', onClick=onClick)

    def press(self):
        if self.selected:
            self.selected = False
            self.state = 'normal'
        else:
            self.selected = True
            self.state = 'pressed'
            self.onClick


class ArrowButton(Button):
    def __init__(self, pos: Vector2, direction: str, onClick=None):
        width = windowWidth / 15
        height = windowHeight / 15
        textures = {
            'right': pygame.transform.scale(pygame.image.load('Assets/Menu/Icons/right.png'),
                                            (width, height)),
            'left': pygame.transform.scale(pygame.image.load('Assets/Menu/Icons/left.png'),
                                           (width, height))
        }
        super().__init__(pos, width, height, textures, direction, onClick=onClick)
