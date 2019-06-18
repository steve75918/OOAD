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
        for propertyName in search_spec.get_properties().keys():
            # java use equals() to advoid key check
            if propertyName not in self._properties.keys():
                return False

            if self._properties[propertyName] != search_spec.get_property(propertyName):
                return False

        return True
