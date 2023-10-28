import pygame

from constants import windowWidth, windowHeight
from Game.game import Game

pygame.init()

# Set window size and caption
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Roboarena')
clock = pygame.time.Clock()

game = Game(window, clock)
game.run()

pygame.quit()
