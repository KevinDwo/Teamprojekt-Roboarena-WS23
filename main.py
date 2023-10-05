import pygame

movementWidth = 20

pygame.init()
#sets Window Size and Caption
window = pygame.display.set_mode((640,480))
pygame.display.set_caption('Roboarena')
clock = pygame.time.Clock()

x = 120
y = 120
running = True

#movement on button contol
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                break
        elif event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_RIGHT:
                    x += movementWidth
                case pygame.K_LEFT:
                    x -= movementWidth
                case pygame.K_DOWN:
                    y += movementWidth
                case pygame.K_UP:
                    y -= movementWidth

    #change background color and draw player
    window.fill((0,0,0))
    pygame.draw.rect(window,(0,0,255),(x,y,40,40))

    #update with 60fps
    pygame.display.update()    
    clock.tick(60)

pygame.quit()