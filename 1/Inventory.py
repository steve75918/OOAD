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

    def search(self, search_spec):
        matching_guitars = list()

        for i in self._guitars:
            # Ignore serial number since that's unique
            guitar_spec = i.get_spec()

            if (search_spec.get_builder() != guitar_spec.get_builder()):
                continue

            model = search_spec.get_model().lower()
            if (not model) and (model != guitar_spec.get_model().lower()):
                continue

            if (search_spec.get_type() != guitar_spec.get_type()):
                continue

            if (search_spec.get_back_wood() != guitar_spec.get_back_wood()):
                continue

            if (search_spec.get_top_wood() != guitar_spec.get_top_wood()):
                continue

            matching_guitars.append(i)

        # did not get anything return false
        return matching_guitars;