from Instrument import *
from GuitarSpec import *

class Guitar(Instrument):
    _serial_number = '10000'
    _price         = 0.0
    _spec          = None

    def __init__(self, serial_number, price, spec):
        super().__init__(serial_number, price, spec)

    # return an GuitarSpec
    def get_spec(cls)->GuitarSpec:
        return cls._spec