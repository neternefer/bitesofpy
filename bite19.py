from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    '''
    Write a simple Promo class. Its constructor receives a name str and expires datetime.

    Add a property called expired which returns a bool.
    '''
    def __init__(self, string, dt):
        self.string = string
        self.dt = dt
        self.expired = NOW > self.dt

    

past_time = NOW - timedelta(seconds=3)
twitter_promo = Promo('twitter', past_time)
print(twitter_promo.expired)
   

