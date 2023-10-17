import pygame
from pygame import Vector2
from Arena.arena import Arena

from Robot.robot import Robot
from State.gameState import GameState

class UserInterface():
    def __init__(self) -> None:
        self.gameState = GameState()
        self.movementCommand = Vector2(0,0)
        self.mousePosition = Vector2(0,0)

        pygame.init()
        # sets Window Size and Caption
        self.window = pygame.display.set_mode((self.gameState.worldWidth(), self.gameState.worldHeight()))
        pygame.display.set_caption('Roboarena')
        self.clock = pygame.time.Clock()
        self.running = True

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
        pressed = pygame.key.get_pressed()
        self.movementCommand = Vector2(0, 0)
        if pressed[pygame.K_RIGHT]:
            self.movementCommand.x += self.gameState.movementWidth
        if pressed[pygame.K_LEFT]:
            self.movementCommand.x += -self.gameState.movementWidth
        if pressed[pygame.K_DOWN]:
            self.movementCommand.y += self.gameState.movementWidth
        if pressed[pygame.K_UP]:
            self.movementCommand.y += -self.gameState.movementWidth
            
        # gets mause position
        self.mousePosition = pygame.mouse.get_pos()
        self.mousePosition = Vector2(self.mousePosition[0],self.mousePosition[1])
        
    
    def render(self):
        # change background color
        self.window.fill((0, 0, 0))
        self.gameState.arena.draw(self.window)
        self.gameState.robot.draw(self.window)
        
        pygame.display.update()
        
    def update(self):
        self.gameState.update(self.movementCommand,self.mousePosition)
        
    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            # update with 60fps
            self.clock.tick(60)

userInterface = UserInterface()
userInterface.run()
pygame.quit()
