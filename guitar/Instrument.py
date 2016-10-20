from abc import *

class Instrument(metaclass=ABCMeta):
    def __init__(cls, serial_number, price, spec):
        cls._serial_number = serial_number
        cls._price         = price
        cls._spec          = spec

    def get_serial_number(cls):
        return cls._serial_number

    def get_price(cls):
        return cls._price

    def set_price(cls, value):
        cls._price = value

    def get_spec(cls):
        return cls._spec