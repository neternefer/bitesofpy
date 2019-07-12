import unittest, datetime
from bite16 import PYBITES_BORN, gen_special_pybites_dates as g

class TestPyDates(unittest.TestCase):
    def test_py_dates(self):
        self.assertEqual(g()[0], datetime.datetime(2017, 3, 29, 0, 0))
        self.assertEqual(g()[3], datetime.datetime(2017, 12, 19, 0, 0))
        self.assertEqual(g()[4], datetime.datetime(2018, 1, 23, 0, 0))
        self.assertEqual(type(g()[0]), datetime.datetime)
        
        
    
    
        
