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

    def equals(self, obj: object)->bool:
        if isinstance(obj, Connection):
            return (self.station1.equals(obj.get_station1()) 
                and self.station2.equals(obj.get_station2()) 
                and (self.line_name.casefold() == obj.get_line_name().casefold()))
        else:
            return False