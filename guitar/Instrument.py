from abc import *
from InstrumentSpec import *

class Instrument(metaclass=ABCMeta):
    def __init__(cls, serial_number:str, price:float, spec):
        cls._serial_number = serial_number
        cls._price         = price
        cls._spec          = spec

    def get_serial_number(cls)->str:
        return cls._serial_number

    def get_price(cls)->float:
        return cls._price

    def set_price(cls, value:float):
        cls._price = value

    # return an InstrumentSpec
    def get_spec(cls)->InstrumentSpec:
        return cls._spec