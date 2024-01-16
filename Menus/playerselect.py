import pygame
from pygame import Surface, Vector2
from pygame.time import Clock

from constants import windowHeight, windowWidth
from Menus.buttons import MenuButton
from Menus.panel import PlayerSelectField, Title
from Menus.menuaction import MenuAction, MenuActionQuit, MenuActionMenu


class PlayerSelect:
    SelectedPlayerTiles = [0, 1]

    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock
        self.backgroundImage = pygame.transform.scale(pygame.image.load('Assets/Menu/menuBackground3.jpg'),
                                                      window.get_size())
        self.title = Title()
        self.playerSelectionFields = [PlayerSelectField(0, 'Player 1', PlayerSelect.SelectedPlayerTiles[0]),
                                      PlayerSelectField(1, 'Player 2', PlayerSelect.SelectedPlayerTiles[1])]

    def process(self) -> MenuAction:
        mainMenuBtnWidth = 500
        btnHeight = 70
        btnSpace = 20

        mainMenuButton = MenuButton(Vector2((windowWidth - mainMenuBtnWidth) / 2,
                                            windowHeight - btnHeight - btnSpace),
                                    'Main Menu', 60,
                                    MenuActionMenu())

        while True:
            mousePosition = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return MenuActionQuit()
                for field in self.playerSelectionFields:
                    nextButton = field.buttons['nextButton']
                    backButton = field.buttons['backButton']
                    updateNextButton(nextButton, mousePosition, event)
                    updateBackButton(backButton, mousePosition, event)
                    returnAction = updateMainMenuButton(mainMenuButton, mousePosition, event)
                    if returnAction:
                        return returnAction

            PlayerSelect.SelectedPlayerTiles[0] = self.playerSelectionFields[0].tileIndex
            PlayerSelect.SelectedPlayerTiles[1] = self.playerSelectionFields[1].tileIndex

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                return MenuActionMenu()

            self.window.blit(self.backgroundImage, (0, 0))
            self.title.draw(self.window)
            for field in self.playerSelectionFields:
                field.draw(self.window)
            mainMenuButton.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)


def updateNextButton(button, mousePosition, event):
    if button.isOver(mousePosition):
        if event.type == pygame.MOUSEBUTTONUP:
            button.onClick()


def updateBackButton(button, mousePosition, event):
    if button.isOver(mousePosition):
        if event.type == pygame.MOUSEBUTTONUP:
            button.onClick()


def updateMainMenuButton(button, mousePosition, event):
    isOver = button.isOver(mousePosition)
    button.state = 'hover' if isOver else 'normal'
    if isOver and (event.type == pygame.MOUSEBUTTONUP):
        return button.onClick
