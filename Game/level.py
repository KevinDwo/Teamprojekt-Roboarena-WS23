from typing import List

from pygame import Vector2, Rect
from tmx import LayerTile, TileMap, Layer

from constants import tileWidth, tileHeight
from Game.Entities.robot import BasicRobot


def decodeLayer(tileMap: TileMap, layer: Layer):
    gid = None
    for tile in layer.tiles:
        if tile.gid != 0:
            gid = tile.gid
            break
    if gid is None:
        tileset = tileMap.tilesets[0]
    else:
        tileset = None
        for t in tileMap.tilesets:
            if gid >= t.firstgid and gid < t.firstgid + t.tilecount:
                tileset = t
                break
        return tileset


def decodeUnitsLayer(state, tileMap: TileMap):
    units = []
    count = 1
    for layer in tileMap.layers:
        if layer.name == "Player1" or layer.name == "Player2":
            tileset = decodeLayer(tileMap, layer)
            source = tileset.image.source
            for y in range(tileMap.height):
                for x in range(tileMap.width):
                    tile = layer.tiles[x + y * tileMap.width]
                    if tile.gid == 0:
                        continue
                    # This is how tileX and tileY can be calculated. They are not used so far.
                    # lid = tile.gid - tileset.firstgid
                    # tileX = lid % tileset.columns
                    # tileY = lid // tileset.columns
                    unit = BasicRobot(state,
                                      source,
                                      Vector2(x * tileMap.height,
                                              y * tileMap.width),
                                      count)
                    count += 1
                    units.append(unit)
    return units


def decodeObstacleLayer(tileMap: TileMap) -> List[Rect]:
    obstacles = []
    for layer in tileMap.layers:
        if layer in tileMap.layers:
            if layer.name == 'Obstacles':
                for y in range(tileMap.height):
                    for x in range(tileMap.width):
                        tile: LayerTile = layer.tiles[x+y * tileMap.width]
                        if tile.gid == 0:
                            continue
                        tilePosition = Vector2(x, y) * tileMap.width
                        obstacles.append(Rect(tilePosition.x, tilePosition.y, tileWidth, tileHeight))
            elif layer.name == 'WallsLowerHalf':
                for y in range(tileMap.height):
                    for x in range(tileMap.width):
                        tile: LayerTile = layer.tiles[x+y * tileMap.width]
                        if tile.gid == 0:
                            continue
                        tilePosition = Vector2(x, y) * tileMap.width
                        obstacles.append(Rect(tilePosition.x, tilePosition.y + tileHeight / 2, tileWidth, tileHeight / 2))
            elif layer.name == 'WallsLeftQuarter':
                for y in range(tileMap.height):
                    for x in range(tileMap.width):
                        tile: LayerTile = layer.tiles[x+y * tileMap.width]
                        if tile.gid == 0:
                            continue
                        tilePosition = Vector2(x, y) * tileMap.width
                        obstacles.append(Rect(tilePosition.x, tilePosition.y, tileWidth / 4, tileHeight))
            elif layer.name == 'WallsRightQuarter':
                for y in range(tileMap.height):
                    for x in range(tileMap.width):
                        tile: LayerTile = layer.tiles[x+y * tileMap.width]
                        if tile.gid == 0:
                            continue
                        tilePosition = Vector2(x, y) * tileMap.width
                        obstacles.append(Rect(tilePosition.x + 3 * tileWidth / 4, tilePosition.y, tileWidth / 4, tileHeight))
    return obstacles


def decodeDeadlylayer(tileMap: TileMap) -> List[Rect]:
    deadly = []
    for layer in tileMap.layers:
        if layer in tileMap.layers:
            if layer.name == 'Deadly':
                for y in range(tileMap.height):
                    for x in range(tileMap.width):
                        tile = layer.tiles[x+y * tileMap.width]
                        if tile.gid == 0:
                            continue
                        tilePosition = Vector2(x, y) * tileMap.width
                        deadly.append(Rect(tilePosition.x, tilePosition.y, tileWidth, tileHeight))
    return deadly
