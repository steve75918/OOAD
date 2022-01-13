from gsf.unit.unit import Unit


class UnitGroup:
    def __init__(self, unitList: list):
        self.units = {}

        for unit in unitList:
            units[unit.id] = unit

        pass

    def getUnitCounts(self):
        return len(self.units)

    def addUnit(self, unit):
        if not isinstance(unit, Unit):
            raise TypeError('Please insert an Unit')

        self.units[unit.id] = unit

        return True

    def getUnit(self, id: int):
        if not isinstance(id, int):
            TypeError('Not an id')

        return self.units[id]

    def getUnits(self):
        return self.units

    def removeUnit(self, unit):
        if isinstance(unit, Unit):
            self.removeUnit(unit.id)
        elif isinstance(unit, int):
            self.remove(unit)
        else:
            raise TypeError('Unidentify unit with id')

        return True

    def remove(self, id: int):
        if id not in self.units.keys():
            raise TypeError('Invalid Id')

        del self.units[id]

        return True
