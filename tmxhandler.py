from pygame import Surface
from pytmx import TiledMap, TiledTileLayer, load_pygame


def load_level(levelPath: str) -> TiledMap:
    return load_pygame(levelPath)


def drawLayer(surface: Surface, tileMap: TiledMap, layerName: str):
    layer: TiledTileLayer = next(x for x in tileMap.layers if x.name == layerName)
    for x, y, gid, in layer:
        tile = tileMap.get_tile_image_by_gid(gid)
        if tile is not None:
            surface.blit(tile, (x * tileMap.tilewidth,
                                y * tileMap.tileheight))
