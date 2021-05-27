import unittest
from ...modules.Connection import Connection
from ...modules.Station import Station
from ...modules.Subway import Subway

class test_subway(unittest.TestCase):
    def setUp(self):
        self.subway = Subway()

        pass

    def test_add_station(self):
        station_name = 'TestStation'
        self.subway.add_station(station_name)

        check_stations = list(filter(lambda s: s.get_name() == station_name, self.subway.stations))
        self.assertTrue(len(check_stations))

        pass
    
    def test_has_station_true(self):
        station_name = 'TestStation'
        result = self.subway.has_station(station_name)

        self.assertTrue(result)

        pass

    def test_has_station_false(self):
        station_name = 'TestNeverListStation'
        result = self.subway.has_station(station_name)

        self.assertFalse(result)

        pass

    def test_add_connection(self):
        station1_name = 'TestStation1'
        station2_name = 'TestStation2'
        line_name     = 'TestLine'

        self.subway.add_station(station1_name)
        self.subway.add_station(station2_name)
        self.subway.add_connection(station1_name, station2_name, line_name)

        station1 = Station(station1_name)
        station2 = Station(station2_name)
        c1 = Connection(station1, station2, line_name)
        c2 = Connection(station2, station1, line_name)

        self.assertTrue(any(c.equals(c1) for c in self.subway.connections))
        self.assertTrue(any(c.equals(c2) for c in self.subway.connections))

        pass

    def tearDown(self):
        del self.subway

        pass