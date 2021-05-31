import unittest
from ...modules.Connection import Connection
from ...modules.Station import Station

class test_connection(unittest.TestCase):
    def setUp(self):
        station1 = Station('TestStation1')
        station2 = Station('TestStation2')
        line     = 'TestLine'

        self.connection = Connection(station1, station2, line)

        pass

    def test_get_line_name(self):
        name = self.connection.get_line_name()

        self.assertIsInstance(name, str)

        pass

    def test_get_station1(self):
        result = self.connection.get_station1()

        self.assertIsInstance(result, Station)

        pass

    def test_get_station2(self):
        result = self.connection.get_station2()

        self.assertIsInstance(result, Station)

        pass

    def test_equals(self):
        c = Connection(Station('TeatConnection1'), Station('TeatConnection2'), 'TestLineName')
        result = (self.connection == c)

        self.assertIsInstance(result, bool)

        pass

    def tearDown(self):
        del self.connection

        pass