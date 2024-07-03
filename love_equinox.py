import datetime
def love_equinox(first_date: datetime.datetime, birthday:datetime.datetime):
    '''Takes two datetime objects and returns the love equinox associated with them.'''
    diff = birthday - first_date
    equinox = first_date - diff

    return equinox