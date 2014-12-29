from Guitar import *

class Inventory:
    # list of Guitar
    _guitars = []

    def __init__(self):
        return

    def add_guitar(self, serial_number, price, builder, model, type, back_wood, top_wood):
        self._guitars.append(Guitar(serial_number, price, builder, model, type, back_wood, top_wood))
        return

    def get_guitar(self, serial_number):
        for i in self._guitars:
            if i.get_serial_number() == serial_number:
                return i;

        # did not get anything return false
        return;

    def search(self, search_obj):
        for i in self._guitars:
            if i.get_serial_number() == serial_number:
                # Ignore serial number since that's unique

                builder = search_obj.get_builder()

                return i;

        # did not get anything return false
        return;