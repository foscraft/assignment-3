import numpy as np

def no_of_weekdays():
    '''
     NumPy program to find the number of weekdays in a given month
     For the month of jan 2022, write/pass str argument `2022-01` as this month(being checked) 
     and `2022-02` as next month (feb)
     '''
    this_month = str(input('enter this month :'))
    next_month = str(input('enter next month :'))
    print ('Number of weekdays in this month are : ',np.busday_count(this_month,next_month))

#invoke function
no_of_weekdays()

