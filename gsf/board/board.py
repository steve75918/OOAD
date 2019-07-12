from gsf.board.tile import Tile
from gsf.unit.unit import Unit

class Board:
    _witdh  = 0
    _height = 0
    _tiles  = []

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._initialize()

    def _initialize(self) -> None:
        self._tiles = [[Tile()] * self._width for i in range(self._height)]

        return None

    def getTile(self, x: int, y: int) -> Tile:
        return self._tiles[x-1][y-1]


    def addUnit(self, unit: Unit, x: int, y: int) -> None:
        tile = self.getTile(x, y)
        tile._addUnit(unit)

        return None

    def removeUnit(self, unit: Unit, x: int, y: int) -> None:
        tile = self.getTile(x, y)
        tile._removeUnit(unit)

        return None

    def removeUnits(self, x: int, y: int) -> None:
        tile = self.getTile(x, y)
        tile._removeUnits()

        return None

    def getUnits(self, x: int, y: int):
        return self.getTile(x, y).getUnits()