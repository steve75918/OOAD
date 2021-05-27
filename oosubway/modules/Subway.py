from .Station import Station
from .Connection import Connection

class Subway():
    stations    = []
    connections = []

    def __init__(self):
        return None

    def add_station(self, station_name: str)->None:
        if not self.has_station(station_name):
            station = Station(station_name)
            self.stations.append(station)

        return None

    def has_station(self, station_name: str)->bool:
        station = Station(station_name)
        
        return any(s.equals(station) for s in self.stations)

    def add_connection(self, station1_name: str, station2_name: str, line_name: str)->None:
        try:
            if not self.has_station(station1_name):
                raise RuntimeError(station1_name + ' does not exist')

            if not self.has_station(station2_name):
                raise RuntimeError(station2_name + ' does not exist')

            station1 = Station(station1_name)
            station2 = Station(station2_name)

            # There are two-way connections between two stations
            connection1 = Connection(station1, station2, line_name)
            connection2 = Connection(station2, station1, line_name)

            self.connections.append(connection1)
            self.connections.append(connection2)
        except RuntimeError as e:
            print('Oops, {0}'.format(e.args))

        return None