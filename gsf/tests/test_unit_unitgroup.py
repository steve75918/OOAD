import unittest
from gsf.unit.unitgroup import UnitGroup
from gsf.unit.unit import Unit


class TestBoardBoard(unittest.TestCase):
    def setUp(self):
        self.unitgroup = UnitGroup([])
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

    def test_removeUnitByUnit(self):
        anyUnit = Unit(1)
        self.unitgroup.addUnit(anyUnit)

        res = self.unitgroup.removeUnit(anyUnit)

        self.assertEqual(True, res)
        self.assertEqual(0, self.unitgroup.getUnitCounts())

        pass

    def test_removeUnitById(self):
        id = 1
        anyUnit = Unit(1)
        self.unitgroup.addUnit(anyUnit)

        res = self.unitgroup.removeUnit(id)

        self.assertEqual(True, res)
        self.assertEqual(0, self.unitgroup.getUnitCounts())

        pass

    def test_removeUnitNotUnit(self):
        anyUnit = Unit(1)
        self.unitgroup.addUnit(anyUnit)

        with self.assertRaises(TypeError):
            res = self.unitgroup.removeUnit(None)

        pass

    def test_removeUnitNotExit(self):
        anyUnit = Unit(1)
        notExistInGroup = Unit(100)
        self.unitgroup.addUnit(anyUnit)

        with self.assertRaises(TypeError):
            res = self.unitgroup.removeUnit(notExistInGroup)

        pass

    def test_getUnitById(self):
        anyUnit = Unit(1)
        self.unitgroup.addUnit(anyUnit)

        res = self.unitgroup.getUnit(1)

        self.assertIsInstance(res, Unit)

        pass

    def test_getUnits(self):
        anyUnit = Unit(1)
        self.unitgroup.addUnit(anyUnit)

        res = self.unitgroup.getUnits()

        self.assertIsInstance(res, dict)
        self.assertEqual(1, len(res))

        pass

    def tearDown(self):
        del self.unitgroup
        pass


if __name__ == '__main__':
    pass
