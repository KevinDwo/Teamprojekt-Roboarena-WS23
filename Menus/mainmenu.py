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
        titleHeight = 100
        btnWidth = 500
        btnHeight = 70
        btnSpace = 20

        title = MenuButton(btnSpace, btnSpace, windowWidth - 2 * btnSpace, titleHeight, 'white', 'ROBOARENA')

        playBtn = MenuButton((windowWidth - btnWidth) / 2, titleHeight + 2 * btnSpace,
                             btnWidth, btnHeight, 'green', 'Play')

        exitBtn = MenuButton((windowWidth - btnWidth) / 2, titleHeight + btnHeight + 3 * btnSpace,
                             btnWidth, btnHeight, 'yellow', 'Exit')

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
