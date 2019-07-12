import unittest
from gsf.board.board import Board
from gsf.board.tile import Tile
from gsf.unit.unit import Unit

class TestBoardBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(3,4)
        pass

    def test_getTile(self):
        anytile = self.board.getTile(0, 1)
        self.assertIsInstance(anytile, Tile)
        pass

    def test_addUnit(self):
        anyUnit = Unit()
        res = self.board.addUnit(anyUnit, 1, 1)

        self.assertIsNone(res)
        pass

    def test_removeUnit(self):
        anyUnit = Unit()
        self.board.addUnit(anyUnit, 1, 1)

        res= self.board.removeUnit(anyUnit, 1, 1)

        self.assertIsNone(res)
        pass

    def test_removeUnits(self):
        for i in range(3):
            self.board.addUnit(Unit(), 1, 1)

        res= self.board.removeUnits(1, 1)

        self.assertIsNone(res)
        pass

    def test_getUnits(self):
        for i in range(3):
            self.board.addUnit(Unit(), 2, 1)

        res = self.board.getUnits(2, 1)

        self.assertIsInstance(res, list)
        pass

    def tearDown(self):
        del self.board
        pass

if __name__ == '__main__':
    pass