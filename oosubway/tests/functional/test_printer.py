import io
import unittest
import unittest.mock

from os import path

from ...modules.printer import Printer
from ...modules.loader import Loader

class test_station(unittest.TestCase):
    def setUp(self):
        self.printer = Printer()

        pass

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, args, expected_output, mock_stdout):
        Printer.print_route(args)
        self.assertTrue(expected_output in mock_stdout.getvalue())


    def test_print_route(self):
        file_path = path.join(path.dirname(__file__), '../test.txt')
        loader = Loader()
        subway = loader.load_from_file(file_path)

        start_station_name = 'TestStation1'
        end_station_name   = 'TestStation6'

        routes = subway.get_directions(start_station_name, end_station_name)

        self.assert_stdout(routes, start_station_name)

        pass

    def tearDown(self):
        del self.printer

        pass