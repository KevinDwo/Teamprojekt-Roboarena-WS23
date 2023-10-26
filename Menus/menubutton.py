import pygame
from pygame import Surface
from typing import Tuple


class MenuButton:
    def __init__(self, x: int, y: int, width: int, height: int, color, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text

    def draw(self, window: Surface):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (0, 0, 0))
        window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos: Tuple[int, int]) -> bool:
        return self.x <= pos[0] and self.x + self.width >= pos[0] and \
               self.y <= pos[1] and self.y + self.height >= pos[1]
