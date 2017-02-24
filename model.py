'''Axis alignment with clocks'''

PRIMARY_AXIS = 'x'

class Axis(object):
    def __init__(self,position=0):
        self._position = position
        self._positions = []

    def position(self,v=0):
        if v:
            self._positions.append(self.position())
            self._position = v
            return self
        return self._position

    def positions(self):
        return self._positions

class Plan(object):
    def __init__(self,*args,**kwargs):
        self._axis = {}
        for (k,v) in kwargs.items():
            self._axis['axis_%s' % (k)] = Axis(v)
        else:
            self._axis['axis_x'] = Axis()
            self._axis['axis_y'] = Axis()

    def axis(self,key_name=PRIMARY_AXIS):
        return self._axis['axis_%s' % (key_name)]

    def axis_count(self):
        return len(self._axis.items())

class Clock(Plan):
    pass
