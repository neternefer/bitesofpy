import unittest
from bite8 import rotate

class TestRotate(unittest.TestCase):
    def test_positive_rotation(self):
        self.assertEqual(rotate('hello', 2), 'llohe')
    def test_negative_rotation(self):
        self.assertEqual(rotate('hello', -2), 'lohel')
