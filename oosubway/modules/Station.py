class Station():
    name = ''

    def __init__(self, station: str):
        self.name = station

        return None

    def get_name(self)->str:
        return self.name

    def equals(self, obj: object)->bool:
        if isinstance(obj, Station):
            return obj.get_name().casefold() == self.name.casefold()
        else:
            return False