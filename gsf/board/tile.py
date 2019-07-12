from gsf.unit.unit import Unit

class Tile:
    _units = []

    def __init__(self):
        pass

    def addUnit(self, unit: Unit) -> None:
        self._units.append(unit)

        return None

    def removeUnit(self, unit: Unit) -> None:
        self._units.remove(unit)

        return None

    def removeUnits(self) -> None:
        self._units.clear()

        return None

    def getUnits(self) -> list:
        return self._units