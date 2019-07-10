from datetime import datetime,  timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    '''
    Write a generator that returns special dates for PyBites:

    Every year mark counting from PYBITES_BORN date
    Every 100 days mark counting from PYBITES_BORN
    result:
    datetime.datetime(2017, 3, 29, 0, 0),
                datetime.datetime(2017, 7, 7, 0, 0),
                datetime.datetime(2017, 10, 15, 0, 0),
                datetime.datetime(2017, 12, 19, 0, 0),
                datetime.datetime(2018, 1, 23, 0, 0),...
    '''
start = PYBITES_BORN
    stop = datetime.now()
    year_gone = PYBITES_BORN + timedelta(days=365)
    result = []
    while start <= stop:
        start += timedelta(days=100)
        result.append(start)
        if start + timedelta(days=100) > year_gone:
            result.append(year_gone)
            year_gone += timedelta(days=365)
    return result
        
gen_special_pybites_dates()
   
