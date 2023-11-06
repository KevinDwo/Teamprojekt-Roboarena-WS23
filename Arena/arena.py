import pygame

from Arena.terrain import Acid, EastWall, Ground, Default, NorthWall, SouthWall, WestWall


class Arena():
    def __init__(self, gameState) -> None:
        self.gameState = gameState
        self.horizontalTiles = int(self.gameState.worldSize.x / self.gameState.tileSize.x)
        self.verticalTiles = int(self.gameState.worldSize.y / self.gameState.tileSize.y)
        # 15 x 13 tiles
        self.loadArena()

    def draw(self, surface):
        for i in range(self.horizontalTiles):
            for j in range(self.verticalTiles):
                tile = self.field[j][i]
                position = pygame.Vector2(i, j)
                position = position.elementwise() * self.gameState.tileSize
                tilePosition = tile.tilePosition.elementwise() * self.gameState.tileSize
                rect = pygame.Rect(tilePosition,self.gameState.tileSize)
                surface.blit(tile.texture,position,rect)

    def loadArena(self):

        # Choose Arena File
        path = 'Arena/Layouts/arena2.txt'

        self.field = [[Default()] * self.horizontalTiles for i in range(self.verticalTiles)]

        with open(path, 'r') as file:
            for i, line in enumerate(file):
                if i >= self.verticalTiles:
                    continue
                line = line.strip()
                for j, symbol in enumerate(line):
                    if j >= self.horizontalTiles:
                        continue
                    match symbol:
                        case 'n': self.field[i][j] = NorthWall()
                        case 's': self.field[i][j] = SouthWall()
                        case 'e': self.field[i][j] = EastWall()
                        case 'w': self.field[i][j] = WestWall()
                        case 'g': self.field[i][j] = Ground()
                        case 'a': self.field[i][j] = Acid()
