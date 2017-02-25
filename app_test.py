'''Axis alignment with clock app test'''

from app import app

import unittest
import requests
import os

class AppTest(unittest.TestCase):
    #def setUp(self):
    #    app.run(host='0.0.0.0',port=8000)

    def test_app_index_route(self):
        index = requests.get('http://0.0.0.0:8000')
        self.assertEqual(index.json(),{'version':'0.0.1'})

if __name__ == '__main__' and 'DEBUG' in os.environ and os.environ['DEBUG'] == 'true':
    unittest.main(verbosity=2)
elif __name__ == '__main__':
    unittest.main()
