import numpy as np
from sys import getsizeof

def array_size():

    '''
    NumPy program to create an array with at least 5 user input integers and
    determine the size of the memory occupied by the array.
    '''
    one = int(input("enter first int :"))
    two = int(input("enter second int :"))
    three = int(input("enter third int :"))
    four = int(input("enter fourth int :"))
    five = int(input("enter fifth int :"))

    arr = np.array([one,two,three,four,five])
    print("memory of the array is : ",getsizeof(arr))

#invoke function
array_size()

