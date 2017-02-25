'''Axis alignment with clock app test'''

from app import app

import unittest
import requests
import os

class AppTest(unittest.TestCase):
    def test_get_app_index_route(self):
        index = requests.get('http://0.0.0.0:8000')
        self.assertEqual(index.json(),{'version':'0.0.1','name':'axis_alignment_with_clocks'})

    def test_get_app_plan_route(self):
        plan = requests.get('http://0.0.0.0:8000/plan')
        self.assertEqual(plan.json(),{'axis':2,'x':0,'y':0})

    def test_get_app_alignment_route(self):
        alignment = requests.get('http://0.0.0.0:8000/alignment')
        self.assertEqual(alignment.json(),{'axis':4,'x':[0,0],'y':[0,0]})

if __name__ == '__main__' and 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
    unittest.main(verbosity=2)
elif __name__ == '__main__':
    unittest.main()
