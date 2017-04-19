from InstrumentSpec import *

class GuitarSpec(InstrumentSpec):
    _num_strings = 0

    def __init__(self, builder, model, type, back_wood, top_wood, num_strings):
        super().__init__(builder, model, type, back_wood, top_wood)
        self._num_strings    = num_strings

    def get_num_strings(self):
        return self._num_strings

    def matches(self, search_spec)->bool:
        if (search_spec.get_builder() != self.get_builder()):
            return False

        model = search_spec.get_model().lower()
        if (not model) and (model != self.get_model().lower()):
            return False

        if (search_spec.get_type() != self.get_type()):
            return False

        if (search_spec.get_back_wood() != self.get_back_wood()):
            return False

        if (search_spec.get_top_wood() != self.get_top_wood()):
            return False

        return True

        