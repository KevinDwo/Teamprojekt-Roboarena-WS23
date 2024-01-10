import pygame
from pygame import Surface, Vector2

from Menus.buttons import MenuButton, PlayerSelectionButton, ArrowButton
from Menus.menuaction import MenuActionMenu, MenuActionQuit
from constants import windowWidth, windowHeight, titleHeight, playerTiles


class Title:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = windowWidth - 2 * 20
        self.height = titleHeight
        self.text = 'RoboArena'
        self.texture = pygame.image.load('Assets/Menu/Panels/Title.png')

    def draw(self, window: Surface):
        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(self.texture, (self.x, self.y, self.width, self.height))
        window.blit(text,
                    (self.x + (self.width/2 - text.get_width()/2),
                        self.y + (self.height/2 - text.get_height()/2)))


class EndScreen:
    def __init__(self, text):
        self.x = windowWidth/2
        self.y = windowHeight/2
        self.width = windowWidth / 2
        self.height = windowHeight / 2
        self.text = text
        self.texture = pygame.transform.scale(pygame.image.load('Assets/Menu/Panels/GameOverScreen.png'),
                                              (self.width, self.height))
        self.rect = self.texture.get_rect()
        self.rect.center = (self.x, self.y)
        self.buttons = [MenuButton(Vector2(0,
                                           self.height / 3), 'Main Menu', MenuActionMenu()),
                        MenuButton(Vector2(0,
                                           2*self.height / 3), 'Quit', MenuActionQuit())]

    def draw(self, window: Surface):
        for event in pygame.event.get():
            for button in self.buttons:
                button.setState('normal')
            mousePosition = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.isOver(mousePosition):
                    button.setState('hover')
                    if event.type == pygame.MOUSEBUTTONUP:
                        return button.onClick
        rect = self.texture.get_rect()
        rect.center = window.get_rect().center
        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (255, 255, 255))
        self.texture.blit(text, (self.width/2 - text.get_width() / 2, text.get_height() / 2))
        # self.buttons[0].draw(self.texture)
        # self.buttons[1].draw(self.texture)
        window.blit(self.texture, rect)


class GameOverScreen(EndScreen):
    def __init__(self):
        super().__init__('Game Over')


class VictoryScreen(EndScreen):
    def __init__(self):
        super().__init__('Victory!')


class PlayerSelectField:
    def __init__(self, index, playerName: str, tileIndex: int):
        self.index = index
        self.position = self.getPosition(index)
        self.width = windowWidth / 3
        self.height = 3 * windowHeight / 4
        self.text = playerName
        self.texture = pygame.transform.scale(pygame.image.load('Assets/Menu/Panels/PlayerSelection.png'),
                                              (self.width, self.height))
        self.tilePosition = self.getTilePosition(index)
        self.tileIndex = tileIndex
        self.buttons = {"selectionButton": PlayerSelectionButton(self.getButtonPosition(index), None),
                        "nextButton": ArrowButton(self.getNextButtonPosition(index), 'right', self.incrementTile),
                        "backButton": ArrowButton(self.getBackButtonPosition(index), 'left', self.decrementTile)}

    def draw(self, window: Surface):
        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (255, 255, 255))
        self.texture.blit(text, (self.width/2 - text.get_width() / 2, text.get_height() / 2))
        window.blit(self.texture, (self.position.x, self.position.y))
        window.blit(scaleTile(getTile(self.tileIndex)), (self.tilePosition.x, self.tilePosition.y))
        for button in self.buttons.values():
            button.draw(window)

    def getButtonPosition(self, index: int) -> Vector2:
        width = windowWidth / 4
        space = 30
        x = index * width + space
        y = 3 * windowHeight / 4 + titleHeight
        return Vector2(x, y)

    def getTilePosition(self, index: int) -> Vector2:
        width = windowWidth / 4
        x = index * width + 20
        y = windowHeight / 2 - titleHeight
        return Vector2(x, y)

    def getPosition(self, index: int) -> Vector2:
        width = windowWidth / 4
        space = 40
        x = index * width - space
        y = titleHeight
        return Vector2(x, y)

    def getNextButtonPosition(self, index: int) -> Vector2:
        width = windowWidth / 4
        space = 20
        x = index * width + windowHeight / 5 - space
        y = 3 * windowHeight / 4 - space
        return Vector2(x, y)

    def getBackButtonPosition(self, index: int) -> Vector2:
        width = windowWidth / 4
        space = 20
        x = index * width + windowHeight / 12 - space
        y = 3 * windowHeight / 4 - space
        return Vector2(x, y)

    def incrementTile(self):
        self.tileIndex = (self.tileIndex + 1) % len(playerTiles)

    def decrementTile(self):
        self.tileIndex = (self.tileIndex - 1) % len(playerTiles)


def getTile(tileIndex: int) -> Surface:
    return playerTiles[tileIndex % len(playerTiles)]


def scaleTile(tile: Surface) -> Surface:
    return pygame.transform.scale(tile, (int(windowWidth / 5), int(windowHeight / 5)))
