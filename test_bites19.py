import unittest
from datetime import datetime, timedelta

from bite19 import NOW, Promo

class TestPromo(unittest.TestCase):
    def setUp(self):
        self.past_time = NOW - timedelta(seconds=3)
        self.current_time = NOW
    def test_expired(self):
        twitter_promo = Promo('twitter', self.past_time)
        self.assertTrue(twitter_promo.expired)
    def test_not_expired(self):
        twitter_promo = Promo('twitter', self.current_time)
        self.assertFalse(twitter_promo.expired)
        
        
        
    
    
        
