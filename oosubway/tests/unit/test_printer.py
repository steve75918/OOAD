import unittest

from ...modules.printer import Printer

class test_station(unittest.TestCase):
    def setUp(self):
        self.printer = Printer()

        pass

    def test_print_route(self):
        result = Printer.print_route([])
    
        self.assertIsNone(result)

        pass

    def tearDown(self):
        del self.printer

        pass