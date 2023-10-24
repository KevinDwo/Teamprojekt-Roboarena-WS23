import pygame
from pygame import Surface, Vector2
from pygame.time import Clock
from Game.gameState import GameState


class Game():
    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock

        # Initiate gamestate enclosing robot and area
        self.gameState = GameState()

    def run(self):
        running = True

        # Movement on button contol
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break

            pressed = pygame.key.get_pressed()

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
            self.gameState.robot.move(movement, self.gameState.worldWidth(),
                                      self.gameState.worldHeight())
            self.gameState.robot.rotate(mousePosition)

            # Set the background color
            self.window.fill((0, 0, 0))
            # Draw field
            self.gameState.arena.draw(self.window)
            # Draws the robot as defined in robot
            self.gameState.robot.draw(self.window)

            # Update with 60fps
            pygame.display.update()
            self.clock.tick(60)
