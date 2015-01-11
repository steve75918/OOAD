class GuitarSpec:
    _builder       = ''
    _model         = ''
    _type          = ''
    _back_wood     = ''
    _top_wood      = ''
    _num_strings    = 0

    def __init__(self, builder, model, type, back_wood, top_wood):
        self._builder        = builder
        self._model          = model
        self._type           = type
        self._back_wood      = back_wood
        self._top_wood       = top_wood

    def get_type(self):
        return self._type

    def get_back_wood(self):
        return self._back_wood

    def get_top_wood(self):
        return self._top_wood

    def get_builder(self):
        return self._builder

    def get_model(self):
        return self._model

    def get_num_strings(self):
        return self._num_strings