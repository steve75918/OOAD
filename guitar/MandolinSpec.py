from InstrumentSpec import *

class MandolinSpec(InstrumentSpec):
    _style       = ''

    def __init__(self, builder, model, type, style, back_wood, top_wood):
        super().__init__(builder, model, type, back_wood, top_wood)
        self._style = style

    def get_style(self):
        return self._style

    def matches(self, search_spec)->bool:
        if not super().matches(search_spec):
            return False

        if not isinstance(search_spec, MandolinSpec):
            return False

        if (search_spec.get_style() != self.get_style()):
            return False

        return True
