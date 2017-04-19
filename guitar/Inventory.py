from Instrument import *

from GuitarSpec import *
from MandolinSpec import *

class Inventory:
    # list of Instrument
    _instruments = list()

    def __init__(self):
        return

    def add_instrument(self, serial_number:str, price:float, spec:InstrumentSpec):
        self._instruments.append(Instrument(serial_number, price, spec))
        return

    def get_instrument(self, serial_number:str)->Instrument:
        for instrument in self._instruments:
            if instrument.get_serial_number() == serial_number:
                return instrument

        # did not get anything return false
        return;

    def search(self, search_spec:GuitarSpec)->list:
        matching_guitars = list()

        for instrument in self._instruments:
            # Ignore serial number since that's unique
            guitar_spec = instrument.get_spec()

            if guitar_spec.matches(search_spec):
                matching_guitars.append(instrument)

        # did not get anything return false
        return matching_guitars

    def search(self, search_spec:MandolinSpec)->list:
        matching_mandolins = list()

        for instrument in self._instruments:
            # Ignore serial number since that's unique
            mandolin_spec = instrument.get_spec()

            if mandolin_spec.matches(search_spec):
                matching_mandolins.append(instrument)

        # did not get anything return false
        return matching_mandolins