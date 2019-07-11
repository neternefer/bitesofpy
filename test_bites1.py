import unittest
from bite1 import sum_numbers

class TestBites(unittest.TestCase):
    def setUp(self):
        self.lst = [5, 1, 4]
    def test_sum_numbers_is_None(self):
        self.assertEqual(sum_numbers(), sum(range(1, 101)))
    def test_sum_numbers_is_list(self):
        self.assertEqual(sum_numbers(self.lst), sum(self.lst))

if __name__ == '__main__':
    unittest.main()
