import pygame

from constants import windowWidth, windowHeight
from Game.game import Game
from Menus.levelselect import LevelSelect
from Menus.mainmenu import MainMenu
from Menus.menuaction import MenuActionMenu, MenuActionPlay, MenuActionQuit, MenuActionSelectLevel, MenuActionPlayerSelect
from Menus.playerselect import PlayerSelect

pygame.init()

# Set window size and caption
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Roboarena')
clock = pygame.time.Clock()

pygame.mixer.music.load('Assets/Sounds/awesomeness.wav')
pygame.mixer.music.play(-1)

action = MenuActionMenu()
while True:
    match action:
        case MenuActionMenu():
            mainMenu = MainMenu(window, clock)
            action = mainMenu.process()

        case MenuActionSelectLevel():
            levelSelect = LevelSelect(window, clock)
            action = levelSelect.show()

        case MenuActionPlay():
            pygame.mixer.music.load('Assets/Sounds/gameMusic1.wav')
            pygame.mixer.music.play(-1)
            game = Game(window, clock, action.level)
            action = game.run()
            pygame.mixer.music.load('Assets/Sounds/awesomeness.wav')
            pygame.mixer.music.play(-1)

        case MenuActionPlayerSelect():
            playerSelect = PlayerSelect(window, clock)
            action = playerSelect.process()

        case MenuActionQuit():
            break

pygame.quit()
