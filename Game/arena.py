import pygame

from Game.terrain import Grass, Mud, Stone, Water


class Arena():
    def __init__(self, gameState) -> None:
        self.gameState = gameState
        self.horizontalTiles = int(self.gameState.worldSize.x / self.gameState.tileSize.x)
        self.verticalTiles = int(self.gameState.worldSize.y / self.gameState.tileSize.y)
        gr, wa, st, md = Grass(), Water(), Stone(), Mud()
        # 15 x 13 tiles
        self.field = [[gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, md, md, md, md, md, md, md, md, md, md, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, wa, wa, wa, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, wa, wa, wa, gr],
                      [gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr, gr],
                      ]

    def draw(self, surface):
        for i in range(self.horizontalTiles):
            for j in range(self.verticalTiles):
                tile = self.field[j][i]
                position = pygame.Vector2(i, j)
                position = position.elementwise() * self.gameState.tileSize
                pygame.draw.rect(surface, tile.color, (position, self.gameState.tileSize))
