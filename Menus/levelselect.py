import re
import os
from typing import Optional
import pygame

from constants import windowHeight, windowWidth
from Menus.menubutton import MenuButton
from Menus.menuaction import MenuAction, MenuActionMenu, MenuActionPlay, MenuActionQuit


class LevelSelect:
    def __init__(self, window, clock):
        self.window = window
        self.clock = clock

    def show(self) -> MenuAction:
        titleHeight = 100
        mainMenuBtnWidth = 500
        btnWidth = 70
        btnHeight = 70
        btnSpace = 20

        title = MenuButton(btnSpace, btnSpace, windowWidth - 2 * btnSpace, titleHeight, 'white', 'Select Level')
        mainMenuBtn = MenuButton((windowWidth - mainMenuBtnWidth) / 2, windowHeight - btnHeight - btnSpace,
                                 mainMenuBtnWidth, btnHeight, 'yellow', 'Main Menu')

        levelButtons = getLevelButtons(btnWidth, btnHeight, btnSpace, titleHeight)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()

                if event.type == pygame.MOUSEBUTTONUP:
                    action = checkMouseClick(event, mainMenuBtn, levelButtons)
                    if action:
                        return action

            self.window.fill((0, 0, 0))
            title.draw(self.window)
            for level in levelButtons.keys():
                levelButtons[level].draw(self.window)
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
            levelButtons[levelNo] = MenuButton(buttonX, buttonY, btnWidth, btnHeight, 'orange', levelNo.lstrip('0'))
            buttonX += btnWidth + btnSpace
            if buttonX + btnWidth + btnSpace > windowWidth:
                buttonX = initialButtonX
                buttonY += btnHeight + btnSpace

    return levelButtons


def checkMouseClick(event, mainMenuBtn, levelButtons) -> Optional[MenuAction]:
    mousePosition = pygame.mouse.get_pos()

    if mainMenuBtn.isOver(mousePosition):
        return MenuActionMenu()

    for level in levelButtons:
        btn = levelButtons[level]
        if btn.isOver(mousePosition):
            return MenuActionPlay(level)
