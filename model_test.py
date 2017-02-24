'''Axis alignment with clocks test'''

import os
import model
import unittest

class DefaultAxisWithoutPositionAsArgumentTest(unittest.TestCase):
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

class AxisWithPositionAsArgumentTest(unittest.TestCase):
    def setUp(self):
        self.axis_x = model.Axis(5)
        self.axis_y = model.Axis(10)
        self.axis_z = model.Axis(15)

    def test_axis_x_instantiation(self):
        self.assertEqual(self.axis_x.__class__,model.Axis)

    def test_axis_y_instantiation(self):
        self.assertEqual(self.axis_y.__class__,model.Axis)

    def test_axis_z_instantiation(self):
        self.assertEqual(self.axis_z.__class__,model.Axis)

    def test_axis_x_position(self):
        self.assertEqual(self.axis_x.position(),5)

    def test_axis_y_poisition(self):
        self.assertEqual(self.axis_y.position(),10)

    def test_axis_z_position(self):
        self.assertEqual(self.axis_z.position(),15)

    def test_axis_x_positions(self):
        self.assertEqual(self.axis_x.positions(),[])
        self.axis_x.position(10)
        self.assertEqual(self.axis_x.position(),10)
        self.assertEqual(self.axis_x.positions(),[5])

    def test_axis_y_position(self):
        self.assertEqual(self.axis_y.positions(),[])
        self.axis_y.position(15)
        self.assertEqual(self.axis_y.position(),15)
        self.assertEqual(self.axis_y.positions(),[10])

    def test_axis_z_position(self):
        self.assertEqual(self.axis_z.positions(),[])
        self.axis_z.position(20)
        self.assertEqual(self.axis_z.position(),20)
        self.assertEqual(self.axis_z.positions(),[15])

class DefaultPlanWithTwoAxisTest(unittest.TestCase):
    def setUp(self):
        self.plan = model.Plan()

    def test_plan_instantiation(self):
        self.assertEqual(self.plan.__class__,model.Plan)

    def test_plan_axis_retrievement(self):
        self.assertEqual(self.plan.axis('x').__class__,model.Axis)
        self.assertEqual(self.plan.axis('y').__class__,model.Axis)

    def test_plan_axis_count(self):
        self.assertEqual(self.plan.axis_count(),2)

class PlanWithThreeAxisTest(unittest.TestCase):
    def setUp(self):
        self.plan = model.Plan(x=10,y=10,z=10)

    def test_plan_instantiation(self):
        self.assertEqual(self.plan.__class__,model.Plan)

    def test_plan_axis_retrievement(self):
        self.assertEqual(self.plan.axis('x').__class__,model.Axis)
        self.assertEqual(self.plan.axis('y').__class__,model.Axis)
        self.assertEqual(self.plan.axis('z').__class__,model.Axis)

#class ClockTest(unittest.TestCase):
#    pass

if __name__ == '__main__' and 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
    unittest.main(verbosity=2)
elif __name__ == '__main__':
    unittest.main()
