import modules

class Example:
    def __init__(self):
        self._vector = modules.vector()

    @property
    def vector(self):
        return self._vector

