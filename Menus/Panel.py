from constants import windowWidth, windowHeight
import pygame
from pygame import Surface


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
