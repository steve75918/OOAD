from gsf.unit.unit import Unit

class UnitGroup:
    def __init__(self):
        self.units = []

        pass

    def getUnitCounts(self):
        return len(self.units)

    def addUnit(self, unit: Unit):
        if not isinstance(unit, Unit):
            raise TypeError('Please insert an Unit')

        self.units.append(unit)

        return True

    def removeUnit(self, unit: Unit):
        if not isinstance(unit, Unit):
            raise TypeError('Please insert an Unit')

        self.units.remove(unit)

        return True