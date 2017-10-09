class InstrumentSpec():
    _properties = None

    def __init__(self, properties):
        # init dict properties
        self._properties = properties

    def get_property(self, property):
        return self._properties.get(property)

    def get_properties(self):
        return self._properties

    def matches(self, search_spec)->bool:
        # 應為讀入 spec 內的屬性後再行比對，但完整比對僅利用 python 內建處理即可
        if search_spec != self._properties:
            return False

        return True
