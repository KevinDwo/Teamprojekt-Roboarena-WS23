from pygame import Vector2
from Game.Entities.robot import BasicRobot


def decodeLayer(tileMap, layer):
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
            if gid >= t.firstgid and gid < t.firstgid+t.tilecount:
                tileset = t
                break
        return tileset


def decodeUnitsLayer(state, tileMap):
    units = []
    count = 1
    for layer in tileMap.layers:
        if layer.name == "Player1" or layer.name == "Player2":
            tileset = decodeLayer(tileMap, layer)
            source = tileset.image.source
            for y in range(tileMap.height):
                for x in range(tileMap.width):
                    tile = layer.tiles[x + y*tileMap.width]
                    if tile.gid == 0:
                        continue
                    lid = tile.gid - tileset.firstgid
                    tileX = lid % tileset.columns
                    tileY = lid // tileset.columns
                    unit = BasicRobot(state,
                                      source,
                                      Vector2(x*tileMap.height,
                                              y*tileMap.width),
                                      Vector2(tileX,
                                              tileY),
                                      count)
                    count += 1
                    units.append(unit)
    return units
