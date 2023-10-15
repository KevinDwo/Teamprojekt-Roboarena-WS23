import pygame

movementWidth = 20

windowWidth = 640
windowHeight = 480

pygame.init()
# sets Window Size and Caption
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Roboarena')
clock = pygame.time.Clock()

x = windowWidth / 2
y = windowHeight / 2

# initialize player
player = pygame.Rect(x, y, 40, 40)

# intitialize coin
coin = pygame.Rect(100, 100, 16, 16)
coinCollected = True

running = True

# movement on button control
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_RIGHT:
                    if x + movementWidth * 2 < windowWidth:
                        x += movementWidth
                case pygame.K_LEFT:
                    if x - movementWidth / 2 > 0:
                        x -= movementWidth
                case pygame.K_DOWN:
                    if y + movementWidth * 2 < windowHeight:
                        y += movementWidth
                case pygame.K_UP:
                    if y - movementWidth / 2 > 0:
                        y -= movementWidth
        # collect coin
        elif player.colliderect(coin):
            coinCollected = False

    # change background color
    window.fill((0, 0, 0))

    # draw coin
    if coinCollected:
        pygame.draw.circle(window, (212, 175, 55), (100, 100), 16)

    # draw player
    player = pygame.Rect(x, y, 40, 40)
    pygame.draw.rect(window, (0, 0, 255), player)

    # update with 60fps
    pygame.display.update()
    clock.tick(60)

pygame.quit()
