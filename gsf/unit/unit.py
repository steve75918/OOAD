from gsf.unit.weapon import Weapon

class Unit:
    type       = ''
    id         = 0
    name       = ''
    weapons    = []
    properties = {}

    def __init__(self, id):
        self.id = id

        pass

    def getId(self) -> int:
        return self.id

    def setType(self, type):
        self.type = type

        return

    def getType(self) -> str:
        return self.type

    def setName(self, name):
        self.name = name

        return

    def getName(self) -> str:
        return self.name

    def addWeapon(self, weapon: Weapon):
        weapons.appen(weapon)
        return

    def getWeapons(self) -> list:
        return self.weapons

    def setProperty(self, key, value):
        self.properties.update({key: value})
        return

    def getProperty(self, key):
        return self.properties.get(key)