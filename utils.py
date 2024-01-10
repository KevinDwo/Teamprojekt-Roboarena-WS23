from math import sin, cos, radians

from pygame import Vector2

from constants import tileHeight, tileWidth


def clamp(x: int, minimum: int, maximum: int) -> int:
    """Returns x if x ∊ [minimum, maximum], otherwise minimum if x is smaller and maximum if x is larger than that."""
    return min(max(x, minimum), maximum)


def degreesToUnitVector(degrees: int) -> Vector2:
    """Converts the given direction in degrees ∊ [0, 360) to a vector of length 1 facing that direction."""
    return Vector2(cos(radians(degrees)), sin(radians(degrees)))


def isRightOf(direction1: int, direction2: int) -> bool:
    """Returns True iff direction 1 is to the right (up to 180 degrees) of direction 2. Both directions are ∊ [0, 360)."""
    if direction1 <= 180:
        return (direction2 <= direction1) or (direction2 >= direction1 + 180)
    else:
        return direction1 - 180 <= direction2 <= direction1


def tileCoordinatesToPositionVector(x: float, y: float) -> Vector2:
    """Turns the tile coordinates (e.g. x=2, y=3) into a position vector (e.g. Vector2(64, 96))"""
    return Vector2(x * tileWidth, y * tileHeight)
