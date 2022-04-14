import unittest
from arrays import array_size
from dates import day_dates
from weeks import no_of_weekdays

class TestAssignment(unittest.TestCase):


    def test_array_size(self):
        self.assertNotEqual(array_size(), 'memory of the array is : 145')

    def test_day_dates(self):
        self.assertNotEqual(day_dates(),'Yesterday: 2022-04-13 Today: 2022-04-14 Tomorrow: 2022-04-15')

    def test_no_of_weekdays(self):
        self.assertNotEqual(no_of_weekdays(),'Number of weekdays in this month are :  21')


if __name__ == '__main__':
    unittest.main()