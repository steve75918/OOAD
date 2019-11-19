import unittest
from gsf.unit.unitgroup import UnitGroup
from gsf.unit.unit import Unit

class TestBoardBoard(unittest.TestCase):
    def setUp(self):
        self.unitgroup = UnitGroup()
        pass

    def test_addUnit(self):
        anyUnit = Unit(1)
        res = self.unitgroup.addUnit(anyUnit)

        self.assertEqual(True, res)
        self.assertEqual(1, self.unitgroup.getUnitCounts())

        pass
    
    def test_addNonUnit(self):
        anyUnit = None

        with self.assertRaises(TypeError):
            res = self.unitgroup.addUnit(anyUnit)

        pass

    def test_removeUnit(self):
        anyUnit = Unit(1)
        self.unitgroup.addUnit(anyUnit)

        res = self.unitgroup.removeUnit(anyUnit)

        self.assertEqual(True, res)
        self.assertEqual(0, self.unitgroup.getUnitCounts())

        pass

    def test_removeNonUnit(self):
        anyUnit = Unit(1)
        self.unitgroup.addUnit(anyUnit)

        with self.assertRaises(TypeError):
            res = self.unitgroup.removeUnit(None)

        pass

    def tearDown(self):
        del self.unitgroup
        pass

if __name__ == '__main__':
    pass