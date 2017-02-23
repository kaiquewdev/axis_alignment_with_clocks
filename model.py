'''Axis alignment with clocks'''

PRIMARY_AXIS = 'x'

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

class Plan(object):
    def __init__(self,*args,**kwargs):
        for (k,v) in kwargs.items():
            self[k] = v
        else:
            self.x = Axis()
            self.y = Axis()

    def axis(self,key_name=PRIMARY_AXIS):
        return self.__getattribute__(key_name)

class Clock(object):
    pass
