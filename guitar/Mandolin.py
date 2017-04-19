from Instrument import *
from MandolinSpec import *

class Mandolin(Instrument):
    _serial_number = '10000'
    _price         = 0.0
    _spec          = None

    def __init__(self, serial_number, price, spec):
        super().__init__(serial_number, price, spec)

    # return an MandolinSpec
    def get_spec(cls)->MandolinSpec:
        return cls._spec