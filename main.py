import pygame

from constants import windowWidth, windowHeight
from Game.game import Game
from Menus.mainmenu import MainMenu
from Menus.menuaction import MenuActionMenu, MenuActionPlay, MenuActionQuit

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

        case MenuActionPlay():
            game = Game(window, clock)
            action = game.run()

        case MenuActionQuit():
            break

pygame.quit()
