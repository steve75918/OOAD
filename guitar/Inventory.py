from Guitar import *

class Inventory:
    # list of Guitar
    _guitars = list()

    def __init__(self):
        return

    def add_guitar(self, serial_number, price, spec):
        self._guitars.append(Guitar(serial_number, price, spec))
        return

    def get_guitar(self, serial_number):
        for guitar in self._guitars:
            if guitar.get_serial_number() == serial_number:
                return guitar;

        # did not get anything return false
        return;

    def search(self, search_spec):
        matching_guitars = list()

        for guitar in self._guitars:
            # Ignore serial number since that's unique
            guitar_spec = guitar.get_spec()

            if guitar_spec.matches(search_spec):
                matching_guitars.append(guitar)

        # did not get anything return false
        return matching_guitars;