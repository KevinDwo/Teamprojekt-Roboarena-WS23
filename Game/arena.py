import tmxhandler


class Arena():
    def __init__(self, gameState, level: str) -> None:
        self.gameState = gameState
        self.horizontalTiles = int(self.gameState.worldSize.x / self.gameState.tileSize.x)
        self.verticalTiles = int(self.gameState.worldSize.y / self.gameState.tileSize.y)
        self.tileMap = tmxhandler.load_level(f"Assets/Maps/level{level}.tmx")

    def drawBelowEntities(self, surface):
        self.drawLayers(surface, ["Ground", "Deadly"])

    def drawAboveEntities(self, surface):
        self.drawLayers(surface, ["WallsLowerHalf", "WallsLeftQuarter", "WallsRightQuarter", "Obstacles", "Decoration"])

    def drawLayers(self, surface, layerNames):
        for layerName in layerNames:
            tmxhandler.drawLayer(surface, self.tileMap, layerName)
