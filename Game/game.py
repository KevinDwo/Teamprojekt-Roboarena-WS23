import pygame
from pygame import Surface
from pygame.time import Clock

from Game.gameState import GameState
from Menus.menuaction import MenuAction, MenuActionMenu, MenuActionQuit


class Game():
    def __init__(self, window: Surface, clock: Clock, level: str):
        self.window = window
        self.clock = clock

        # Initiate gamestate enclosing robot and area
        self.gameState = GameState(level)

    def run(self) -> MenuAction:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                return MenuActionMenu()

            # Make every entity handle the key presses relevant to it
            self.gameState.handleKeyPresses(pressed)

            # Move all the entities
            self.gameState.moveEntities()

            # Draw everything to the screen
            self.gameState.draw(self.window)

            # Update with 60fps
            pygame.display.update()
            self.clock.tick(60)
