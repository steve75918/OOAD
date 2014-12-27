from Guitar import *

class Inventory:
    # list of Guitar
    guitars = []

    def __init__(self):
        return

    def add_guitar(self, serial_number, price, builder, model, type, back_wood, top_wood):
        self.guitars.append(Guitar(serial_number, price, builder, model, type, back_wood, top_wood))
        return

    def get_guitar(self, serial_number):
        for i in self.guitars:
            if i.get_serial_number() == serial_number:
                return i;
        # did not get anything return false
        return;

    # def search(obj):
    #     return obj;
    def test(self):
        print(self.guitars)