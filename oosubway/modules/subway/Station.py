class Station():
    name = ''

    def __init__(self, station: str):
        self.name = station

        return None

    def get_name(self)->str:
        return self.name

    def __eq__(self, other: object)->bool:
        if isinstance(other, Station):
            return other.__hash__() == self.__hash__()
        else:
            return False
    
    def __hash__(self):
        return hash(self.name.casefold())