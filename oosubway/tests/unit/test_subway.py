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
        result = self.subway.add_station(station_name)

        self.assertIsNone(result)

        pass

    def test_has_station(self):
        station_name = 'TestStation'
        result = self.subway.has_station(station_name)

        self.assertIsInstance(result, bool)

        pass

    def test_add_connection(self):
        station1_name = 'TestStation1'
        station2_name = 'TestStation2'
        line     = 'TestLine'

        result = self.subway.add_connection(station1_name, station2_name, line)

        self.assertIsNone(result)

        pass

    def tearDown(self):
        del self.subway

        pass