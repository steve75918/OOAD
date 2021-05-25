import unittest
from ...modules.Station import Station

class test_station(unittest.TestCase):
    def setUp(self):
        self.station = Station('TestStation')

        pass

    def test_get_name(self):
        name = self.station.get_name()

        self.assertEqual(name, 'TestStation')

        pass

    def test_equals_true(self):
        another_station = Station('TestStation')
        result = self.station.equals(another_station)

        self.assertEqual(result, True)

        pass

    def test_equals_false(self):
        another_station = Station('TestStation2')
        result = self.station.equals(another_station)

        self.assertEqual(result, False)

        pass

    def test_equals_false_object_type(self):
        another_station = object()
        result = self.station.equals(another_station)

        self.assertEqual(result, False)

        pass

    def tearDown(self):
        del self.station

        pass