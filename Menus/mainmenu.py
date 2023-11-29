import pygame
from pygame import Surface, Vector2
from pygame.time import Clock
from Menus.Panel import Title

from constants import windowWidth, windowHeight
from Menus.menuaction import MenuAction, MenuActionQuit, MenuActionSelectLevel, MenuActionPlayerSelect
from Menus.buttons import MenuButton


class MainMenu:
    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock
        self.backgroundImage = pygame.transform.scale(pygame.image.load('Assets/Menu/menuBackground1.jpg'),
                                                      window.get_size())
        self.title = Title()
        self.buttons = [MenuButton(self.getButtonPosition(1), 'Play', MenuActionSelectLevel()),
                        MenuButton(self.getButtonPosition(2), 'Select Player', MenuActionPlayerSelect()),
                        MenuButton(self.getButtonPosition(3), 'Quit', MenuActionQuit())]

    def process(self) -> MenuAction:
        pygame.mixer.music.load('Assets/Sounds/awesomeness.wav')
        pygame.mixer.music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()
                for button in self.buttons:
                    button.setState('normal')
                mousePosition = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.isOver(mousePosition):
                        button.setState('hover')
                        if event.type == pygame.MOUSEBUTTONUP:
                            return button.onClick

            self.window.blit(self.backgroundImage, (0, 0))
            self.title.draw(self.window)
            self.buttons[0].draw(self.window)
            self.buttons[1].draw(self.window)
            self.buttons[2].draw(self.window)

            pygame.display.update()
            self.clock.tick(60)

    def getButtonPosition(self, index: int) -> Vector2:
        buttonHeight = windowHeight / 10
        buttonWidth = windowWidth / 2
        space = 20
        y = self.title.height + index * (buttonHeight + space)
        x = (windowWidth - buttonWidth) / 2
        return Vector2(x, y)
