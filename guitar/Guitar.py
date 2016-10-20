from Instrument import *
from GuitarSpec import *

class Guitar(Instrument):
    _serial_number = '10000'
    _price         = 0.0
    _spec          = None

    def __init__(self, serial_number, price, spec):
        super(Guitar, self).__init__(serial_number, price, spec)