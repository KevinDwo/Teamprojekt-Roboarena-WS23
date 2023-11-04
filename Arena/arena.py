import pygame

from Arena.terrain import Grass, Mud, Stone, Water, Default


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
                pygame.draw.rect(surface, tile.color, (position, self.gameState.tileSize))
    
    def loadArena(self):
        
        # Choose Arena File
        path = 'Arena/Layouts/arena1.txt'

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
                        case 'w': self.field[i][j] = Water()
                        case 'g': self.field[i][j] = Grass()
                        case 's': self.field[i][j] = Stone()
                        case 'm': self.field[i][j] = Mud()
