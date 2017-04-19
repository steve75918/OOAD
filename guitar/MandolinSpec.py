from InstrumentSpec import *

class MandolinSpec(InstrumentSpec):
    _style       = ''

    def __init__(self, builder, model, type, style, back_wood, top_wood):
        super().__init__(builder, model, type, back_wood, top_wood)
        self._style          = style

    def get_style(self):
        return self._style

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

        