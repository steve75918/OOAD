from gsf.unit.unit import Unit

class Tile:
    _units = []

    def __init__(self):
        pass

    def _addUnit(self, unit: Unit) -> None:
        self._units.append(unit)

        return None

    def _removeUnit(self, unit: Unit) -> None:
        self._units.remove(unit)

        return None