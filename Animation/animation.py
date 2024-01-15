import pygame


class Animation:
    def __init__(self, gameState, tileSetPath: str, position: (int, int) = (0, 0)):
        self.tileSet = pygame.image.load(tileSetPath)
        self.gameState = gameState
        self.tileNumber = 0
        self.tiles = []
        self.position = position

    def draw(self, surface: pygame.Surface, repeat: bool = False):
        tile = self.tiles[int(self.tileNumber / 20)]
        surface.blit(self.tileSet, self.position, tile)
        self.tileNumber += 1
        if self.tileNumber >= len(self.tiles) * 20 and repeat:
            self.tileNumber = 0
        elif self.tileNumber >= len(self.tiles) * 20 and not repeat:
            self.gameState.animations.remove(self)
