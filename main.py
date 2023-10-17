import pygame
from pygame import Vector2


def clamp(x: int, minimum: int, maximum: int) -> int:
    """Returns x if x ∊ [minimum, maximum], otherwise minimum if x is smaller and maximum if x is larger than that."""
    return min(max(x, minimum), maximum)


movementWidth = 5

windowWidth = 640
windowHeight = 480

playerSize = 40

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

    position += movement
    position.x = clamp(position.x, 0, windowWidth - playerSize)
    position.y = clamp(position.y, 0, windowHeight - playerSize)

    # change background color and draw player
    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 0, 255), (position.x, position.y, playerSize, playerSize))

    # update with 60fps
    pygame.display.update()
    clock.tick(60)

pygame.quit()
