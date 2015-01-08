from Guitar import *

class Inventory:
    # list of Guitar
    _guitars = list()

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
        matching_guitars = list()

        for i in self._guitars:
            # Ignore serial number since that's unique

            if (search_obj.get_builder() != i.get_builder()):
                continue

            model = search_obj.get_model().lower()
            if (not model) and (model != i.get_model().lower()):
                continue

            if (search_obj.get_type() != i.get_type()):
                continue

            if (search_obj.get_back_wood() != i.get_back_wood()):
                continue

            if (search_obj.get_top_wood() != i.get_top_wood()):
                continue

            matching_guitars.append(i)

        # did not get anything return false
        return matching_guitars;