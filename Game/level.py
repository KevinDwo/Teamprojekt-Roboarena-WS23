from pygame import Vector2
import tmx

from Game.robot import BasicRobot

def decodeUnitsLayer(state,tileMap):
        """
        Create a list from a tileMap layer
        """  
        units = []
        for l in range(4,6):      
            layer = tileMap.layers[l]
            tileset = tileMap.tilesets[l]
            source = tileset.image.source
            
            for y in range(tileMap.height):
                for x in range(tileMap.width):
                    tile = layer.tiles[x + y*tileMap.width]
                    if tile.gid == 0:
                        continue
                    lid = tile.gid - tileset.firstgid
                    tileX = lid % tileset.columns
                    tileY = lid // tileset.columns
                    unit = BasicRobot(state,Vector2(x*tileMap.height,y*tileMap.width),source,Vector2(tileX,tileY))
                    units.append(unit)

        return units
