import pygame
from pygame import Surface, Vector2
from pygame.time import Clock

from constants import windowWidth, windowHeight, gitHubURL, updateLogUrl
from Menus.buttons import MenuButton, URLButton
from Menus.menuaction import MenuAction, MenuActionMenu, MenuActionQuit
from Menus.panel import Title


class Credits:
    def __init__(self, window: Surface, clock: Clock):
        self.window = window
        self.clock = clock
        self.backgroundImage = pygame.transform.scale(pygame.image.load('Assets/Menu/menuBackground2.jpg'),
                                                      window.get_size())
        self.uniLogo = pygame.image.load('Assets/Unilogo.png')

    def show(self) -> MenuAction:
        mainMenuBtnWidth = 500
        btnHeight = 70
        btnSpace = 20

        mainMenuButton = MenuButton(Vector2((windowWidth - mainMenuBtnWidth) / 2,
                                            windowHeight - btnHeight - btnSpace),
                                    'Main Menu', 60,
                                    MenuActionMenu())

        self.mainMenuButton = mainMenuButton
        self.buttons = [mainMenuButton,
                        URLButton(Vector2(630, 338), 'GitHub Repository', gitHubURL),
                        URLButton(Vector2(630, 498), 'Update Log', updateLogUrl)]
        self.texts = self.getTexts()
        self.title = Title()
        self.defaultCursor = pygame.mouse.get_cursor()

        while True:
            mousePosition = pygame.mouse.get_pos()
            mouseOverButton = next((b for b in self.buttons if b.isOver(mousePosition)), None)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if type(mouseOverButton) is URLButton else self.defaultCursor)

            for button in self.buttons:
                button.state = 'hover' if button is mouseOverButton else 'normal'

            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        return MenuActionQuit()

                    case pygame.MOUSEBUTTONUP:
                        if mouseOverButton is self.mainMenuButton:
                            return MenuActionMenu()
                        elif type(mouseOverButton) is URLButton:
                            mouseOverButton.click()

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_ESCAPE]:
                return MenuActionMenu()

            self.window.blit(self.backgroundImage, (0, 0))
            self.window.blit(self.uniLogo, (40, 575))
            self.title.draw(self.window)
            for text, pos in self.texts:
                self.window.blit(text, pos)
            for button in self.buttons:
                button.draw(self.window)

            pygame.display.update()
            self.clock.tick(60)

    def getTexts(self):
        fontSize = 25
        font = pygame.font.SysFont('arial', fontSize)
        texts = [('by Lucas Augull, Kevin Dworzak, Philip-Daniel Ebsworth and Ludwig Kolesch', (75, 150)),
                 ('Created as team project in the winter term 2023/24 at University of Tübingen.', (30, 250)),
                 ('Supervisor: Timo Sachsenberg', (30, 285)),
                 ('The code is 100% open-source - come check out our', (30, 350)), ('!', (865, 350)),
                 ('Using the PyGame engine and the PyTMX library for loading the levels.', (30, 430)),
                 ('If you are interested in the making process, we documented every step on', (30, 465)),
                 ('our journey!', (30, 500)),
                 ('Read about it in the', (400, 510)),
                 ('Thank you for playing our game!', (565, 630))]

        return [(font.render(text, 1, (255, 255, 255)), pos) for text, pos in texts]
