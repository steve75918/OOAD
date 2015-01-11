from GuitarSpec import *

class Guitar:
    _serial_number = '10000'
    _price         = 0.0
    _spec          = None

    def __init__(self, serial_number, price, spec):
        self._serial_number = serial_number
        self._price         = price
        self._spec          = spec

    def get_serial_number(self):
        return self._serial_number

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def get_spec(self):
        return self._spec