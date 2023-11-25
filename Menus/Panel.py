from constants import windowWidth, windowHeight
import pygame
from pygame import Surface


class Panel:
    def __init__(self, x: int, y: int, width: int, height: int, text: str = ''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.texture = pygame.transform.scale(pygame.image.load("Assets/Menu/ButtonNormal1.png"),
                                              (width, height))

        def draw(self, window: Surface):
            font = pygame.font.SysFont('arial', 60)
            text = font.render(self.text, 1, (255, 255, 255))
            window.blit(self.texture, (self.x, self.y, self.width, self.height))
            window.blit(text,
                        (self.x + (self.width/2 - text.get_width()/2),
                         self.y + (self.height/2 - text.get_height()/2)))


class Title:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = windowWidth - 2 * 20
        self.height = windowHeight / 10
        self.text = 'RoboArena'
        self.texture = pygame.image.load('Assets/Menu/Panels/Title.png')

    def draw(self, window: Surface):
        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(self.texture, (self.x, self.y, self.width, self.height))
        window.blit(text,
                    (self.x + (self.width/2 - text.get_width()/2),
                        self.y + (self.height/2 - text.get_height()/2)))
