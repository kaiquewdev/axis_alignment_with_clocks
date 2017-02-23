'''Axis alignment with clocks test'''

import os
import model
import unittest

class AxisTest(unittest.TestCase):
    def setUp(self):
        self.axis = model.Axis()

    def test_axis_instantiation(self):
        self.assertEqual(self.axis.__class__,model.Axis)

    def test_axis_position(self):
        self.assertEqual(self.axis.position(),0)
        self.axis.position(5)
        self.assertEqual(self.axis.position(),5)

    def test_axis_positions(self):
        self.assertEqual(self.axis.positions(),[])
        self.assertEqual(self.axis.position(),0)
        self.axis.position(5)
        self.assertEqual(self.axis.positions(),[0])
        self.axis.position(10)
        self.assertEqual(self.axis.positions(),[0,5])

class PlanTest(unittest.TestCase):
    def setUp(self):
        #self.x = model.Axis()
        #self.y = model.Axis()
        self.plan = model.Plan()

    def test_plan_instantiation(self):
        self.assertEqual(self.plan.__class__,model.Plan)
        self.assertEqual(self.plan.x.__class__,model.Axis)
        self.assertEqual(self.plan.y.__class__,model.Axis)

class ClockTest(unittest.TestCase):
    pass

if __name__ == '__main__' and 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
    unittest.main(verbosity=2)
elif __name__ == '__main__':
    unittest.main()
