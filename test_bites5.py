import unittest
from bite5 import NAMES, dedup_and_title_case_names, sort_by_surname_desc,\
                  shortest_first_name

second_result = ['Julian Sequeira', 'Arnold Schwarzenegger',
                 'Keanu Reeves', 'Julbob Pybites', 'Brad Pitt',
                 'Al Pacino', 'Matt Damon', 'Sandra Bullock',
                 'Bob Belderbos', 'Alec Baldwin']

class TestNamesList(unittest.TestCase):
    
    def setUp(self):
        self.unique = dedup_and_title_case_names(NAMES)
        self.sorted = sort_by_surname_desc(NAMES)
        self.shortest = shortest_first_name(NAMES)

    def test_title_names(self):
        pass
    def test_unique_names(self):
        self.assertEqual(self.unique,\
                         [name.title() for name in list(set(NAMES))])
    def test_sorted_names(self):
        self.assertEqual(self.sorted, second_result)
    def test_shortest_name(self):
        self.assertEqual(self.shortest, 'Al')
