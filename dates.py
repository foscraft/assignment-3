import numpy as np

def day_dates():
    '''
    NumPy program to get the dates of yesterday, today and tomorrow.
    '''

    yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
    today = np.datetime64('today', 'D')
    tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
    print( "Yesterday:", yesterday,
           "Today:", today,
           "Tomorrow:", tomorrow)

#invoking the function
day_dates()