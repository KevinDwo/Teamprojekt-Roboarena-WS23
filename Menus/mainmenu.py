import pygame
from pygame import Surface, Vector2
from pygame.time import Clock

from constants import windowWidth, windowHeight
from Menus.menuaction import MenuAction, MenuActionQuit, MenuActionSelectLevel, MenuActionPlayerSelect, MenuActionCredits
from Menus.buttons import MenuButton
from Menus.panel import Title


class MainMenu:
    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock
        self.backgroundImage = pygame.transform.scale(pygame.image.load('Assets/Menu/menuBackground1.jpg'),
                                                      window.get_size())
        self.title = Title()
        self.buttons = [MenuButton(self.getButtonPosition(1), 'Play', 60, MenuActionSelectLevel()),
                        MenuButton(self.getButtonPosition(2), 'Select Player', 60, MenuActionPlayerSelect()),
                        MenuButton(self.getButtonPosition(3), 'Credits', 60, MenuActionCredits()),
                        MenuButton(self.getButtonPosition(4), 'Quit', 60, MenuActionQuit())]

    def process(self) -> MenuAction:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()
                for button in self.buttons:
                    button.state = 'normal'
                mousePosition = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.isOver(mousePosition):
                        button.state = 'hover'
                        if event.type == pygame.MOUSEBUTTONUP:
                            return button.onClick

            self.window.blit(self.backgroundImage, (0, 0))
            self.title.draw(self.window)
            for b in self.buttons:
                b.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)

    def getButtonPosition(self, index: int) -> Vector2:
        buttonHeight = windowHeight / 10
        buttonWidth = windowWidth / 2
        space = 20
        y = self.title.height + index * (buttonHeight + space)
        x = (windowWidth - buttonWidth) / 2
        return Vector2(x, y)
