import unittest
from os import path

from ...modules.loader import Loader

class test_loader(unittest.TestCase):
    def setUp(self):
        self.loader = Loader()

        pass

    def test_load_from_file(self):
        file_path = path.join(path.dirname(__file__), '../test.txt')
        subway = self.loader.load_from_file(file_path)

        self.assertEqual(len(subway.stations), 10)
        self.assertEqual(len(subway.connections), 26)

        pass

    def tearDown(self):
        del self.loader

        pass