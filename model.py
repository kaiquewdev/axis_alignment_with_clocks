'''Axis alignment with clocks'''

class Axis(object):
    def __init__(self):
        self._position = 0
        self._positions = []

    def position(self,v=0):
        if v:
            self._positions.append(self.position())
            self._position = v
        return self._position

    def positions(self):
        return self._positions

class Base(object):
    pass

class Clock(object):
    pass
