import pygame
from pygame import Surface
from pygame.time import Clock

from constants import windowWidth
from Menus.menuaction import MenuAction, MenuActionQuit, MenuActionSelectLevel
from Menus.menubutton import MenuButton


class MainMenu:
    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock

    def show(self) -> MenuAction:
        buttonWidth = 500
        buttonHeight = 70

        title = MenuButton(20, 20, windowWidth - 40, 100, 'white', 'ROBOARENA')
        playBtn = MenuButton((windowWidth - buttonWidth) / 2, 150, buttonWidth, buttonHeight, 'green', 'Play')
        exitBtn = MenuButton((windowWidth - buttonWidth) / 2, 240, buttonWidth, buttonHeight, 'yellow', 'Exit')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()

                if event.type == pygame.MOUSEBUTTONUP:
                    mousePosition = pygame.mouse.get_pos()
                    if playBtn.isOver(mousePosition):
                        return MenuActionSelectLevel()

                    if exitBtn.isOver(mousePosition):
                        return MenuActionQuit()

            self.window.fill((0, 0, 0))
            title.draw(self.window)
            playBtn.draw(self.window)
            exitBtn.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)
