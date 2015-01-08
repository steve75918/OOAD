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
            # Ignore serial number since that's unique

            builder = search_obj.get_builder()
            if (not builder) and (builder != i.get_builder()):
                continue

            model = search_obj.get_model().lower()
            if (not model) and (model != i.get_model().lower()):
                continue

            type = search_obj.get_type()
            if (not type) and (type != i.get_type()):
                continue

            back_wood = search_obj.get_back_wood()
            if (not back_wood) and (back_wood != i.get_back_wood()):
                continue

            top_wood = search_obj.get_top_wood()
            if (not top_wood) and (top_wood != i.get_top_wood()):
                continue

            return;

        # did not get anything return false
        return;