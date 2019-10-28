import unittest
from gsf.unit.unit import Unit
from gsf.unit.weapon import Weapon

class TestUnitUnit(unittest.TestCase):
    def testGetId(self):
        unit = Unit(1)

        id = unit.getId()
        self.assertEqual(id, 1)

        pass

    def testName(self):
        unit = Unit(1)
        unit.setName('Damon')

        name = unit.getName()
        self.assertEqual(name, 'Damon')

        pass

    def testType(self):
        unit = Unit(1)
        unit.setType('infantry')

        type = unit.getType()
        self.assertEqual(type, 'infantry')

        pass

    def testProperty(self):
        unit = Unit(1)
        unit.setProperty('hitPoints', 25)

        hp = unit.getProperty('hitPoints')
        self.assertEqual(hp, 25)

        pass

    def testPropertyChange(self):
        unit = Unit(1)
        unit.setProperty('hitPoints', 25)

        # change
        unit.setProperty('hitPoints', 15)

        hp = unit.getProperty('hitPoints')
        self.assertEqual(hp, 15)

        pass

    def testPropertyNonExist(self):
        unit = Unit(1)

        str = unit.getProperty('strength')

        self.assertEqual(str, None)

        pass

if __name__ == '__main__':
    pass