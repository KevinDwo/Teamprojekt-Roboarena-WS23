from pygame import Vector2
from Animation.animation import Animation

from constants import *

class BulletExplosion(Animation):
    def __init__(self, gameState, position: Vector2):
        super().__init__(gameState, "Assets\projectiles.png", position=position)
        self.tiles = [None] * 4
        for i in range(0, 4):
            self.tiles[i] = pygame.Rect(tileWidth * i, tileHeight * 7, tileWidth, tileHeight)
        
        