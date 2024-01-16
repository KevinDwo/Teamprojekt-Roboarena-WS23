import pygame
from pygame import Surface, Vector2

from Menus.buttons import GameEndButton, ArrowButton
from Menus.menuaction import MenuActionMenu, MenuActionQuit
from constants import windowWidth, windowHeight, titleHeight, playerTiles


class Title:
    TitleTexture = pygame.image.load('Assets/Menu/Panels/Title.png')

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = windowWidth - 40
        self.height = titleHeight
        self.text = 'Roboarena'

    def draw(self, window: Surface):
        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (255, 255, 255))
        window.blit(self.TitleTexture, (self.x, self.y, self.width, self.height))
        window.blit(text, (self.x + (self.width/2 - text.get_width()/2),
                           self.y + (self.height/2 - text.get_height()/2)))


class EndScreen:
    def __init__(self, text):
        self.x = windowWidth / 4
        self.y = windowHeight / 4
        self.width = windowWidth / 2
        self.height = windowHeight / 2
        self.text = text
        self.texture = pygame.transform.scale(pygame.image.load('Assets/Menu/Panels/GameOverScreen.png'),
                                              (self.width, self.height))
        self.rect = self.texture.get_rect()
        self.rect.center = Vector2(windowWidth / 2, windowHeight / 2)
        self.buttons = [GameEndButton(Vector2(self.x + windowWidth / 12,
                                              self.y + self.height / 3), 'Main Menu', 40, MenuActionMenu()),
                        GameEndButton(Vector2(self.x + windowWidth / 12,
                                              self.y + 3 * self.height / 5), 'Quit', 40, MenuActionQuit())]

    def draw(self, window: Surface):
        mousePosition = pygame.mouse.get_pos()
        mouseOverButton = next((b for b in self.buttons if b.isOver(mousePosition)), None)
        for button in self.buttons:
            if button.isOver(mousePosition):
                button.state = 'hover' if button is mouseOverButton else 'normal'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return MenuActionQuit()

            if event.type == pygame.MOUSEBUTTONUP:
                if mouseOverButton:
                    return mouseOverButton.onClick

        font = pygame.font.SysFont('arial', 60)
        text = font.render(self.text, 1, (255, 255, 255))
        self.texture.blit(text, (self.width/2 - text.get_width() / 2, text.get_height() / 2))
        window.blit(self.texture, self.rect)
        self.buttons[0].draw(window)
        self.buttons[1].draw(window)


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
        self.buttons = {"nextButton": ArrowButton(self.getNextButtonPosition(index), 'right', self.incrementTile),
                        "backButton": ArrowButton(self.getBackButtonPosition(index), 'left', self.decrementTile)}

    def draw(self, window: Surface):
        font = pygame.font.SysFont('arial', 40)
        text = font.render(self.text, 1, (255, 255, 255))
        self.texture.blit(text, (self.width/2 - text.get_width() / 2, text.get_height() / 2 + 10))
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
