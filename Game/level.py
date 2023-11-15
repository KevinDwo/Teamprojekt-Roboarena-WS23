from pygame import Vector2
import tmx

from Game.Entities.robot import BasicRobot


def decodeUnitsLayer(state,tileMap):
        """
        Create a list from a tileMap layer
        """  
        units = []
        selected = True
        count = 1
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
                    unit = BasicRobot(state,source,Vector2(x*tileMap.height,y*tileMap.width),Vector2(tileX,tileY),count,selected)
                    #only sets firs player to true
                    count += 1
                    if selected:
                        selected = False
                    units.append(unit)

        return units
