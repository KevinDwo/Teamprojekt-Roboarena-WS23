import pygame

from Arena.terrain import Grass, Mud, Stone, Water


class Arena():
    def __init__(self) -> None:
        self.arenaSize = pygame.Vector2(1000,1000)
        self.tileSize = pygame.Vector2(50,50)
        self.horizontalTiles = int(self.arenaSize.x / self.tileSize.x)
        self.verticalTiles = int(self.arenaSize.y / self.tileSize.y)
        gr, wa, st ,md = Grass(), Water(), Stone(), Mud()
        self.field = [[gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,md,md,md,md,md,md,md,md,md,md,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,wa,wa,wa,wa,wa,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,st,gr,gr,wa,wa,wa,wa,wa,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,st,gr,gr,wa,wa,wa,wa,wa,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,st,gr,gr,wa,wa,wa,wa,wa,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,st,gr,gr,wa,wa,wa,wa,wa,gr,gr],
                      [gr,gr,gr,gr,gr,st,st,st,st,st,st,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                      [gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr,gr],
                     ]
        
    def draw(self, surface):
        for i in range(self.horizontalTiles):
            for j in range(self.verticalTiles):
                tile = self.field[j][i]
                position = pygame.Vector2(i,j)
                position = position.elementwise() * self.tileSize
                pygame.draw.rect(surface,tile.color,(position,tile.size))