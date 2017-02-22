'''Axis alignment with clocks test'''

import os
import model
import unittest

class AxisTest(unittest.TestCase):
    def setUp(self):
        self.axis = model.Axis()

    def test_axis_instantiation(self):
        self.assertEqual(self.axis.__class__,model.Axis)

class BaseTest(unittest.TestCase):
    pass

class ClockTest(unittest.TestCase):
    pass

if __name__ == '__main__' and 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
    unittest.main(verbosity=2)
elif __name__ == '__main__':
    unittest.main()
