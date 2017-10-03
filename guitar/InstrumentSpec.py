class InstrumentSpec():
    _properties = None

    def __init__(self, builder, model, type, back_wood, top_wood):
        # init dict properties
        self._properties =

    def get_property(self, property):
        return self._properties.get(property)

    def get_properties():
        return self._properties

    def matches(self, search_spec)->bool:
        # 應為讀入 spec 內的屬性後再行比對
        # if (search_spec.get_builder() != self.get_builder()):
        #     return False

        # model = search_spec.get_model().lower()
        # if (not model) and (model != self.get_model().lower()):
        #     return False

        # if (search_spec.get_type() != self.get_type()):
        #     return False

        # if (search_spec.get_back_wood() != self.get_back_wood()):
        #     return False

        # if (search_spec.get_top_wood() != self.get_top_wood()):
        #     return False

        return True
