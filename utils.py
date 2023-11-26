from math import sin, cos, radians

from pygame import Vector2

from constants import tileHeight, tileWidth


def clamp(x: int, minimum: int, maximum: int) -> int:
    """Returns x if x ∊ [minimum, maximum], otherwise minimum if x is smaller and maximum if x is larger than that."""
    return min(max(x, minimum), maximum)


def degreesToUnitVector(degrees: int) -> Vector2:
    """Converts the given direction in degrees ∊ [0, 360) to a vector of length 1 facing that direction"""
    return Vector2(cos(radians(degrees)), sin(radians(degrees)))


def collisionDetection(playerPosition: Vector2, obstaclePosition: Vector2) -> bool:
    return playerPosition.x - tileWidth/2 <= obstaclePosition.x <= playerPosition.x + tileWidth/2 and \
            playerPosition.y - tileWidth/2 <= obstaclePosition.y <= playerPosition.y + tileHeight/2


def isPlayerLeft(player) -> bool:
    for robot in player:
        if robot.isAlive:
            return True
    return False
