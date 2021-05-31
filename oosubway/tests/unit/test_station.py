import unittest
from ...modules.Station import Station

class test_station(unittest.TestCase):
    def setUp(self):
        self.station = Station('TestStation')

        pass

    def test_get_name(self):
        name = self.station.get_name()

        self.assertIsInstance(name, str)

        pass

    def test_equals(self):
        another_station = Station('TestStation2')
        result = (self.station == another_station)

        self.assertIsInstance(result, bool)

        pass

    def tearDown(self):
        del self.station

        pass