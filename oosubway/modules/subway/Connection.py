from .Station import Station

class Connection():
    line_name = ''
    station1  = None
    station2  = None

    def __init__(self, station1: Station, station2: Station, line: str):
        self.station1  = station1
        self.station2  = station2
        self.line_name = line

        return None

    def get_station1(self)->Station:
        return self.station1
    
    def get_station2(self)->Station:
        return self.station2
    
    def get_line_name(self)->str:
        return self.line_name

    def __eq__(self, other: object)->bool:
        if isinstance(other, Connection):
            return self.__hash__() == other.__hash__()
        else:
            return False

    def __hash__(self):
        return hash((self.station1.get_name().casefold(), 
            self.station2.get_name().casefold(), 
            self.line_name.casefold()
        ))