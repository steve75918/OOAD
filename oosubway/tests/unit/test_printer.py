import unittest

from ...modules.printer import Printer

class test_printer(unittest.TestCase):
    def setUp(self):
        self.printer = Printer()

        pass

    def tearDown(self):
        del self.printer

        pass