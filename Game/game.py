import pygame
from pygame import Surface, Vector2
from pygame.time import Clock
from Game.gameState import GameState
from Menus.menuaction import MenuAction, MenuActionMenu, MenuActionQuit


class Game:
    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock
        # Initiate gamestate enclosing robot and area
        self.gameState = GameState()

    def checkKeyPresses(self, pressed) -> tuple[Vector2, int]:
        """Handle game relevant key presses, returns the movement vector for the
           current game loop iteration."""
        if pressed[pygame.K_1]:
            self.gameState.selectRobot(0)
        elif pressed[pygame.K_2]:
            self.gameState.selectRobot(1)
        elif pressed[pygame.K_3]:
            self.gameState.selectRobot(2)
        elif pressed[pygame.K_4]:
            self.gameState.selectRobot(3)

        # Movement on button control
        movement = Vector2(0, 0)
        direction = 0
        if pressed[pygame.K_RIGHT]:
            direction += self.gameState.getActiveRobot().computeDirection()
        if pressed[pygame.K_LEFT]:
            direction -= self.gameState.getActiveRobot().computeDirection()
        if pressed[pygame.K_DOWN]:
            movement += -self.gameState.getActiveRobot().computeMovement()
        if pressed[pygame.K_UP]:
            movement += self.gameState.getActiveRobot().computeMovement()

        return movement, direction

    def run(self) -> MenuAction:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                return MenuActionMenu()

            movement = self.checkKeyPresses(pressed)[0]
            direction = self.checkKeyPresses(pressed)[1]

            # Move and rotate the robot
            self.gameState.update(movement, direction)

            # Draw everything to the screen
            self.gameState.draw(self.window)

            # Update with 60fps
            pygame.display.update()
            self.clock.tick(60)
