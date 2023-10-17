import pygame
from pygame import Vector2

from Robot.robot import Robot

movementWidth = 5

windowWidth = 640
windowHeight = 480

#initiate Robot
robot = Robot()

pygame.init()
# sets Window Size and Caption
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Roboarena')
clock = pygame.time.Clock()

position = Vector2(windowWidth / 2, windowHeight / 2)
running = True

# movement on button contol
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
    # gets mause position
    mousePosition = pygame.mouse.get_pos()
    mousePosition = Vector2(mousePosition[0],mousePosition[1])
    
    #moves and rotates the robot
    robot.move(movement)
    robot.rotate(mousePosition)
    

    # change background color
    window.fill((0, 0, 0))
    
    #draws the robot as defined in robot
    robot.draw(window)

    # update with 60fps
    pygame.display.update()
    clock.tick(60)

pygame.quit()
