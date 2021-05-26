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

        self.assertEqual(name, 'TestLine')

        pass

    def test_get_station1(self):
        result = self.connection.get_station1()

        self.assertEqual(result.get_name(), 'TestStation1')

        pass

    def test_get_station2(self):
        result = self.connection.get_station2()

        self.assertEqual(result.get_name(), 'TestStation2')

        pass

    def test_equals_true(self):
        c = Connection(Station('TestStation1'), Station('TestStation2'), 'TestLine')
        result = self.connection.equals(c)

        self.assertTrue(result)

        pass

    def test_equals_false(self):
        c = Connection(Station('TeatConnection1'), Station('TeatConnection2'), 'TestLineName')
        result = self.connection.equals(c)

        self.assertFalse(result)

        pass

    def tearDown(self):
        del self.connection

        pass