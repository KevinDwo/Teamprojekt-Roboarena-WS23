import re
import os

import pygame
from pygame import Vector2

from constants import windowHeight, windowWidth
from Menus.buttons import LevelButton, MenuButton
from Menus.menuaction import MenuAction, MenuActionMenu, MenuActionPlay, MenuActionQuit
from Menus.panel import Title


class LevelSelect:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock
        self.backgroundImage = pygame.transform.scale(pygame.image.load('Assets/Menu/menuBackground2.jpg'),
                                                      window.get_size())

    def show(self) -> MenuAction:
        titleHeight = 100
        mainMenuBtnWidth = 500
        btnWidth = 70
        btnHeight = 70
        btnSpace = 20

        title = Title()
        mainMenuBtn = MenuButton(Vector2((windowWidth - mainMenuBtnWidth) / 2,
                                         windowHeight - btnHeight - btnSpace),
                                 'Main Menu',
                                 MenuActionMenu())

        self.buttons = getLevelButtons(btnWidth, btnHeight, btnSpace, titleHeight)
        self.buttons['mainMenu'] = mainMenuBtn
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()
            for button in self.buttons.values():
                button.setState('normal')
            mousePosition = pygame.mouse.get_pos()
            for button in self.buttons.values():
                if button.isOver(mousePosition):
                    button.setState('hover')
                    if event.type == pygame.MOUSEBUTTONUP:
                        return button.onClick

            self.window.blit(self.backgroundImage, (0, 0))
            title.draw(self.window)
            for level in self.buttons.keys():
                self.buttons[level].draw(self.window)
            mainMenuBtn.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)


levelFileRegex = re.compile(r'^level(\d+).tmx')


def getLevelButtons(btnWidth, btnHeight, btnSpace, titleHeight):
    levelButtons = {}

    # Ensure that the buttons are centered when the row is full
    initialButtonX = btnSpace + ((windowWidth - btnSpace) % (btnWidth + btnSpace)) / 2
    buttonX = initialButtonX
    buttonY = titleHeight + 2 * btnSpace

    for arena in sorted(os.listdir('Assets/Maps')):
        m = levelFileRegex.match(arena)
        if m:
            levelNo = m.group(1)
            levelButtons[levelNo] = LevelButton(Vector2(buttonX, buttonY), levelNo.lstrip('0'), MenuActionPlay(levelNo))
            buttonX += btnWidth + btnSpace
            if buttonX + btnWidth + btnSpace > windowWidth:
                buttonX = initialButtonX
                buttonY += btnHeight + btnSpace

    return levelButtons
