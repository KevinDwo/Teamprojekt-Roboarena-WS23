from math import sin, cos, radians

from pygame import Vector2


def degreesToUnitVector(degrees: int) -> Vector2:
    """Converts the given direction in degrees ∊ [0, 360) to a vector of length 1 facing that direction."""
    return Vector2(cos(radians(degrees)), sin(radians(degrees)))


def isRightOf(direction1: int, direction2: int) -> bool:
    """Returns True iff direction 1 is to the right (up to 180 degrees) of direction 2. Both directions are ∊ [0, 360)."""
    if direction1 <= 180:
        return (direction2 <= direction1) or (direction2 >= direction1 + 180)
    else:
        return direction1 - 180 <= direction2 <= direction1
