import pygame
from pygame import Vector2
from State.gameState import GameState

# Initiate gamestate enclosing robot and area
gameState = GameState()

pygame.init()

# Set window size and caption
window = pygame.display.set_mode((gameState.worldWidth(),
                                  gameState.worldHeight()))
pygame.display.set_caption('Roboarena')
clock = pygame.time.Clock()

position = Vector2(gameState.worldWidth() / 2, gameState.worldHeight() / 2)
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
        movement.x += gameState.movementWidth
    if pressed[pygame.K_LEFT]:
        movement.x += -gameState.movementWidth
    if pressed[pygame.K_DOWN]:
        movement.y += gameState.movementWidth
    if pressed[pygame.K_UP]:
        movement.y += -gameState.movementWidth

    # Get the mouse position
    mousePosition = pygame.mouse.get_pos()
    mousePosition = Vector2(mousePosition[0], mousePosition[1])

    # Move and rotate the robot
    gameState.robot.move(movement, gameState.worldWidth(),
                         gameState.worldHeight())
    gameState.robot.rotate(mousePosition)

    # Set the background color
    window.fill((0, 0, 0))
    # Draw field
    gameState.arena.draw(window)
    # Draws the robot as defined in robot
    gameState.robot.draw(window)

    # Update with 60fps
    pygame.display.update()
    clock.tick(60)

pygame.quit()
