import pygame
from pygame import Vector2
from Robot.robot import BasicRobot

movementWidth = 5

windowWidth = 640
windowHeight = 480

# Initiate robot
robot = BasicRobot()

pygame.init()

# Set window size and caption
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Roboarena')
clock = pygame.time.Clock()

position = Vector2(windowWidth / 2, windowHeight / 2)
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
        movement.x += movementWidth
    if pressed[pygame.K_LEFT]:
        movement.x += -movementWidth
    if pressed[pygame.K_DOWN]:
        movement.y += movementWidth
    if pressed[pygame.K_UP]:
        movement.y += -movementWidth

    # Get the mouse position
    mousePosition = pygame.mouse.get_pos()
    mousePosition = Vector2(mousePosition[0], mousePosition[1])

    # Move and rotate the robot
    robot.move(movement, windowWidth, windowHeight)
    robot.rotate(mousePosition)

    # Set the background color
    window.fill((0, 0, 0))

    # Draw the robot on the window
    robot.draw(window)

    # Update with 60fps
    pygame.display.update()
    clock.tick(60)

pygame.quit()
