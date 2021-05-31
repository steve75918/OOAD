import unittest
from os import path

from ...modules.Loader import Loader
from ...modules.Subway import Subway

class test_loader(unittest.TestCase):
    def setUp(self):
        self.loader = Loader()

        pass

    def test_load_from_file(self):
        file_path = path.join(path.dirname(__file__), '../test.txt')
        result = self.loader.load_from_file(file_path)

        self.assertIsInstance(result, Subway)

        pass

    def tearDown(self):
        del self.loader

        pass