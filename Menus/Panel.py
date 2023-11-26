from Menus.buttons import MenuButton
from Menus.menuaction import MenuActionMenu, MenuActionQuit
from constants import windowWidth, windowHeight
import pygame
from pygame import Surface, Vector2


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


class GameOverScreen:
    def __init__(self):
        self.x = windowWidth/2
        self.y = windowHeight/2
        self.width = windowWidth / 2
        self.height = windowHeight / 2
        self.text = 'Game Over'
        self.texture = pygame.transform.scale(pygame.image.load('Assets/Menu/Panels/GameOverScreen.png'),
                                              (self.width, self.height))
        self.rect = self.texture.get_rect()
        self.rect.center = (self.x, self.y)
        self.buttons = [MenuButton(Vector2(0,
                                           self.height / 3), 'Main Menu', MenuActionMenu()),
                        MenuButton(Vector2(0,
                                           2*self.height / 3), 'Quit', MenuActionQuit())]

    def draw(self, window: Surface):
        for event in pygame.event.get():
            for button in self.buttons:
                button.setState('normal')
            mousePosition = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.isOver(mousePosition):
                    button.setState('hover')
                    if event.type == pygame.MOUSEBUTTONUP:
                        return button.onClick
        rect = self.texture.get_rect()
        rect.center = window.get_rect().center
        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (255, 255, 255))
        self.texture.blit(text, (self.width/2 - text.get_width() / 2, text.get_height() / 2))
        # self.buttons[0].draw(self.texture)
        # self.buttons[1].draw(self.texture)
        window.blit(self.texture, rect)
