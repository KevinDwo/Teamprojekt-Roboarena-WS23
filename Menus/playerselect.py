import pygame
from pygame import Surface
from pygame.time import Clock
from Menus.Panel import PlayerSelectField, Title
from Menus.menuaction import MenuAction, MenuActionQuit, MenuActionMenu


class PlayerSelect:
    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock
        self.backgroundImage = pygame.transform.scale(pygame.image.load('Assets/Menu/menuBackground3.jpg'),
                                                      window.get_size())
        self.title = Title()
        self.playerSelectionFields = [PlayerSelectField(0, 'Player 1', 0),
                                      PlayerSelectField(1, 'Player 2', 1),
                                      PlayerSelectField(2, 'Player 3', 2),
                                      PlayerSelectField(3, 'Player 4', 3)]

    def process(self) -> MenuAction:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()
                mousePosition = pygame.mouse.get_pos()
                for field in self.playerSelectionFields:
                    selectionButton = field.buttons['selectionButton']
                    nextButton = field.buttons['nextButton']
                    backButton = field.buttons['backButton']
                    updateSelectionButton(selectionButton, mousePosition, event)
                    updateNextButton(nextButton, mousePosition, event)
                    updateBackButton(backButton, mousePosition, event)
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                return MenuActionMenu()

            self.window.blit(self.backgroundImage, (0, 0))
            self.title.draw(self.window)
            for field in self.playerSelectionFields:
                field.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)


def updateSelectionButton(button, mousePosition, event):
    if not button.selected:
        button.setState('normal')
    if button.isOver(mousePosition):
        if not button.selected:
            button.setState('hover')
        if event.type == pygame.MOUSEBUTTONUP:
            button.press()


def updateNextButton(button, mousePosition, event):
    if button.isOver(mousePosition):
        if event.type == pygame.MOUSEBUTTONUP:
            button.press()


def updateBackButton(button, mousePosition, event):
    if button.isOver(mousePosition):
        if event.type == pygame.MOUSEBUTTONUP:
            button.press()
