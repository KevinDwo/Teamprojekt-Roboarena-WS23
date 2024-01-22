from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from Game.gameState import GameState

from pygame import Rect, Surface
from pytmx import TiledMap, TiledTileLayer, load_pygame

from constants import tileWidth, tileHeight, playerTiles
from Game.Entities.robot import BasicRobot
from Game.Entities.enemy import Enemy
from Menus.playerselect import PlayerSelect
from utils import tileCoordinatesToPositionVector


def loadLevel(levelPath: str) -> TiledMap:
    """Load a level TileMap with all information about the arena and its entities from a .tmx file."""
    return load_pygame(levelPath)


def drawLayer(surface: Surface, tileMap: TiledMap, layerName: str):
    """Draw the layer in tileMap that matches the given layerName onto the given pygame surface."""
    layer: TiledTileLayer = next(x for x in tileMap.layers if x.name == layerName)
    for x, y, gid, in layer:
        tile = tileMap.get_tile_image_by_gid(gid)
        if tile is not None:
            surface.blit(tile, (x * tileMap.tilewidth,
                                y * tileMap.tileheight))


def decodeRobotsLayers(state: 'GameState') -> List[BasicRobot]:
    """Creates the playable robot objects at the correct starting positions defined in the game state."""
    tileMap: TiledMap = state.arena.tileMap
    robots = []

    robotLayerNames = [name for name in sorted(tileMap.layernames.keys()) if name.startswith("Player")]
    robotLayers: List[TiledTileLayer] = [tileMap.get_layer_by_name(name) for name in robotLayerNames]

    for i, layer in enumerate(robotLayers):
        x, y, _ = next(layer.tiles())
        img = playerTiles[PlayerSelect.SelectedPlayerTiles[i]]
        robots.append(BasicRobot(state, img, tileCoordinatesToPositionVector(x, y), i + 1))

    return robots


def decodeEnemyLayer(state: 'GameState') -> List[Enemy]:
    """Creates the enemy objects at the correct starting positions defined in the game state."""
    tileMap = state.arena.tileMap
    enemies = []

    enemyLayer: TiledTileLayer = tileMap.get_layer_by_name("Enemies")
    for x, y, img in enemyLayer.tiles():
        enemies.append(Enemy(state, img, tileCoordinatesToPositionVector(x, y)))

    return enemies


def decodeObstacleLayer(state: 'GameState') -> List[Rect]:
    """Creates a list of all rectangles in the game arena that are obstacles (entities cannot pass through)."""
    tileMap = state.arena.tileMap
    obstacles = []

    obstacleLayer: TiledTileLayer = tileMap.get_layer_by_name('Obstacles')
    wallsLowerHalfLayer: TiledTileLayer = tileMap.get_layer_by_name('WallsLowerHalf')
    wallsLeftQuarterLayer: TiledTileLayer = tileMap.get_layer_by_name('WallsLeftQuarter')
    wallsRightQuarterLayer: TiledTileLayer = tileMap.get_layer_by_name('WallsRightQuarter')

    for x, y, _img in obstacleLayer.tiles():
        tilePosition = tileCoordinatesToPositionVector(x, y)
        obstacles.append(Rect(tilePosition.x, tilePosition.y, tileWidth, tileHeight))
    for x, y, _img in wallsLowerHalfLayer.tiles():
        tilePosition = tileCoordinatesToPositionVector(x, y)
        obstacles.append(Rect(tilePosition.x, tilePosition.y + tileHeight / 2, tileWidth, tileHeight / 2))
    for x, y, _img in wallsLeftQuarterLayer.tiles():
        tilePosition = tileCoordinatesToPositionVector(x, y)
        obstacles.append(Rect(tilePosition.x, tilePosition.y, tileWidth / 4, tileHeight))
    for x, y, _img in wallsRightQuarterLayer.tiles():
        tilePosition = tileCoordinatesToPositionVector(x, y)
        obstacles.append(Rect(tilePosition.x + 3 * tileWidth / 4, tilePosition.y, tileWidth / 4, tileHeight))

    return obstacles


def decodeDeadlylayer(state: 'GameState') -> List[Rect]:
    """Creates a list of all rectangles in the game arena that are deadly (players get area damage)."""
    tileMap = state.arena.tileMap
    deadly = []

    deadlyLayer: TiledTileLayer = tileMap.get_layer_by_name('Deadly')
    for x, y, _img in deadlyLayer.tiles():
        tilePosition = tileCoordinatesToPositionVector(x, y)
        deadly.append(Rect(tilePosition.x, tilePosition.y, tileWidth, tileHeight))

    return deadly
