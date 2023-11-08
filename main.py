import pygame

from constants import windowWidth, windowHeight
from Game.game import Game
from Menus.levelselect import LevelSelect
from Menus.mainmenu import MainMenu
from Menus.menuaction import MenuActionMenu, MenuActionPlay, MenuActionQuit, MenuActionSelectLevel

pygame.init()

# Set window size and caption
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Roboarena')
clock = pygame.time.Clock()

action = MenuActionMenu()
while True:
    match action:
        case MenuActionMenu():
            mainMenu = MainMenu(window, clock)
            action = mainMenu.show()

        case MenuActionSelectLevel():
            levelSelect = LevelSelect(window, clock)
            action = levelSelect.show()

        case MenuActionPlay():
            game = Game(window, clock, action.level)
            action = game.run()

        case MenuActionQuit():
            break

pygame.quit()
