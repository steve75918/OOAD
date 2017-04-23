from InstrumentSpec import *

class GuitarSpec(InstrumentSpec):
    _num_strings = 0

    def __init__(self, builder, model, type, back_wood, top_wood, num_strings):
        super().__init__(builder, model, type, back_wood, top_wood)
        self._num_strings    = num_strings

    def get_num_strings(self):
        return self._num_strings

    def matches(self, search_spec)->bool:
        if not super().matches(search_spec):
            return False

        if not isinstance(search_spec, GuitarSpec):
            return False

        if (search_spec.get_num_strings() != self.get_num_strings()):
            return False

        return True
