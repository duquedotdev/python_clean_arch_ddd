from ValueObject import ValueObject

class Identifier(ValueObject):
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value