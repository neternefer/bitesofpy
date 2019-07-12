import unittest
from bite15 import names, countries, enumerate_names_countries as e
 
output = '''1. Julian     Australia
            2. Bob        Spain
            3. PyBites    Global
            4. Dante      Argentina
            5. Martin     USA
            6. Rodolfo    Mexico'''

class Test(unittest.TestCase):
    def test_enumerate_names(self):
        self.assertEqual(e().split('\n')[0], '1. Julian     Australia')
        
        
    
    
        
