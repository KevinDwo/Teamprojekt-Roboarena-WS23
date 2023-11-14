import pygame
from pygame import Surface, Vector2
from pygame.time import Clock

from Game.gameState import GameState
from Menus.menuaction import MenuAction, MenuActionMenu, MenuActionQuit


class Game():
    def __init__(self, window: Surface, clock: Clock, level: str):
        self.window = window
        self.clock = clock
        # Initiate gamestate enclosing robot and area
        self.gameState = GameState(level)

        # Speed/Acceleration for Robot movement
        self.currentSpeed = 0
        self.maxSpeed = 4
        self.acceleration = 0.05
        self.currentRotationalSpeed = 0
        self.maxRotationalSpeed = 1.6
        self.rotationalAcceleration = 0.02

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
        direction = 0
        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
            self.currentRotationalSpeed = min(self.currentRotationalSpeed + self.rotationalAcceleration,
                                              self.maxRotationalSpeed)
        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self.currentRotationalSpeed = max(self.currentRotationalSpeed - self.rotationalAcceleration,
                                              -self.maxRotationalSpeed)
        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
            self.currentSpeed = max(self.currentSpeed - self.acceleration, 0)
        if pressed[pygame.K_UP] or pressed[pygame.K_w]:
            self.currentSpeed = min(self.currentSpeed + self.acceleration, self.maxSpeed)

        movement = self.gameState.getActiveRobot().computeMovement() * self.currentSpeed
        direction += self.currentRotationalSpeed
        return movement, direction

    def run(self) -> MenuAction:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()

            pressed = pygame.key.get_pressed()

            if pressed[pygame.K_ESCAPE]:
                return MenuActionMenu()

            movement, direction = self.checkKeyPresses(pressed)

            # Move and rotate the robot
            self.gameState.update(movement, direction)

            # Draw everything to the screen
            self.gameState.draw(self.window)

            # Update with 60fps
            pygame.display.update()
            self.clock.tick(60)
