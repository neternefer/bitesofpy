from pytz import timezone, utc
import datetime as dt

AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    au = naive_utc_dt.astimezone(AUSTRALIA)
    sp = naive_utc_dt.astimezone(SPAIN)
    return (au, sp)


what_time_lives_pybites(dt.datetime.now()) 

