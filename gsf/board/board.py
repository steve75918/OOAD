from gsf.board import Tile
from gsf.unit import Unit

class Board:
    _witdh  = 0
    _height = 0
    _tiles  = []

    def __init__(cls, width: int, height: int):
        cls._width = width
        cls._height = height
        cls._initialize()

    def _initialize() -> None:
        cls._tiles = [[Tiles()] * cls._width for i in range(cls._height)]

        return None

    def getTile(cls, x: int, y: int) -> Tile:
        return cls._tiles[x-1][y-1]


    def addUnit(cls, unit: Unit, x: int, y: int) -> None:
        tile = cls.getTile(x, y)
        tile.addUnit(unit)

        return None

    def removeUnit(cls, unit: Unit, x: int, y: int) -> None:
        tile = cls.getTile(x, y)
        tile.removeUnit(unit)

        return None

    def removeUnits(cls, x: int, y: int) -> None:
        tile = cls.getTile(x, y)
        tile.removeUnits()

        return None

    def getUnits(cls, x: int, y: int):
        return cls.getTile(x, y).getUnits()