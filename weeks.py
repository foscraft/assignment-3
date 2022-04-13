import numpy as np

def no_of_weekdays(this_month,next_month):
    '''
     NumPy program to find the number of weekdays in a given month
     For the month of jan 2022, write/pass str argument `2022-01` as this month(being checked) 
     and `2022-02` as next month (feb)
     '''
    print ('Number of weekdays in this month are : ',np.busday_count(this_month,next_month))

#invoke function
no_of_weekdays('2022-01', '2022-02')

