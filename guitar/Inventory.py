from Instrument import *


class Inventory:
    # list of Instrument
    _instruments = list()

    def __init__(self):
        return

    def add_instrument(self, serial_number: str, price: float, spec: InstrumentSpec):
        instrument = Instrument(serial_number, price, spec)

        self._instruments.append(instrument)

        return

    def get_instrument(self, serial_number: str)->Instrument:
        for instrument in self._instruments:
            if instrument.get_serial_number() == serial_number:
                return instrument

        # did not get anything return false
        return

    # search guitar
    def search(self, search_spec: InstrumentSpec)->list:
        matching_instruments = list()

        for instrument in self._instruments:
            # Ignore serial number since that's unique
            instrument_spec = instrument.get_spec()

            if instrument.get_spec().matches(search_spec):
                matching_instruments.append(instrument)

        # did not get anything return false
        return matching_instruments
