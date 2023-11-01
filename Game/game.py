import pygame
from pygame import Surface, Vector2
from pygame.time import Clock
from Game.gameState import GameState
from Menus.menuaction import MenuAction, MenuActionMenu, MenuActionQuit


class Game():
    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock

        # Initiate gamestate enclosing robot and area
        self.gameState = GameState()

    def run(self) -> MenuAction:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                return MenuActionMenu()

            # Movement on button contol
            movement = Vector2(0, 0)
            if pressed[pygame.K_RIGHT]:
                movement.x += self.gameState.movementWidth
            if pressed[pygame.K_LEFT]:
                movement.x += -self.gameState.movementWidth
            if pressed[pygame.K_DOWN]:
                movement.y += self.gameState.movementWidth
            if pressed[pygame.K_UP]:
                movement.y += -self.gameState.movementWidth

            # Get the mouse position
            mousePosition = pygame.mouse.get_pos()
            mousePosition = Vector2(mousePosition[0], mousePosition[1])

            # Move and rotate the robot
            self.gameState.update(movement, mousePosition)

            # Draw everything to the screen
            self.gameState.draw(self.window)

            # Update with 60fps
            pygame.display.update()
            self.clock.tick(60)
