from typing import List, NewType
from .Station import Station
from .Connection import Connection

class Subway():
    stations    = set()
    connections = set()
    network     = dict()

    def __init__(self):
        self.stations    = set()
        self.connections = set()
        self.network     = dict()
        
        return None

    def add_station(self, station_name: str)->None:
        if not self.has_station(station_name):
            station = Station(station_name)
            self.stations.add(station)

        return None

    def has_station(self, station_name: str)->bool:
        station = Station(station_name)
        
        return any(s == station for s in self.stations)

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

            self.connections.add(connection1)
            self.connections.add(connection2)

            self.add_to_network(station1, station2)
            self.add_to_network(station2, station1)
        except RuntimeError as e:
            print('Oops, {0}'.format(e.args))

        return None
    
    def add_to_network(self, station1: Station, station2: Station)->None:
        # check key exist
        if station1.get_name() in self.network:
            connectedStations = self.network.get(station1.get_name())
            connectedStations.add(station2)
        else:
            connectedStations = {station2}
            self.network[station1.get_name()] = connectedStations
        
        return None
    
    def get_directions(self, start_station_name: str, end_station_name: str)->list:
        # check stations exist
        if not self.has_station(start_station_name) or not self.has_station(end_station_name):
            raise RuntimeError(start_station_name + ' or ' + end_station_name + ' does not exist')

        # use sort of A* to find one path on graph, no garantee of distance
        # because in such information, we can not estamate cost
        start = Station(start_station_name)
        end   = Station(end_station_name)

        openList  = set()
        closeList = set()
        previousStations = dict()

        try:
            # tier 1
            neighbors = self.network.get(start.get_name())
            for neighbor in neighbors:
                previousStations[neighbor.get_name()] = start
                if neighbor != end:
                    openList.add(neighbor)
                else:
                    raise Exception('Founded')

            closeList.add(start)

            # others
            for station in list(openList):
                neighbors = self.network.get(station.get_name()) - closeList

                for neighbor in neighbors:
                    previousStations[neighbor.get_name()] = station
                    if neighbor != end:
                        openList.add(neighbor)
                    else:
                        raise Exception('Founded')
                
                closeList.add(station)
        except Exception as e:
            pass
        
        # after build data, find path and store into routes
        routes = list()
        foundRoute = False
        
        station1 = end
        station2 = previousStations.get(end.get_name())

        while not foundRoute:
            routes.append(self.get_connection(station2, station1))

            if station2 == start:
                foundRoute = True
            
            station1 = station2
            station2 = previousStations.get(station2.get_name())
        
        routes.reverse()
            
        return routes

    def get_connection(self, station1: Station, station2: Station)->Connection:
        for connection in self.connections:
            if connection.get_station1() == station1 and connection.get_station2() == station2:
                return connection

        return None