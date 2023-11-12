#Creating the Test Case
from django.test import SimpleTestCase
from app import calc

#Creating a class based on SimpleTestCase 
class CalcTest(SimpleTestCase):
#Creating a method of class to calculate result of two numbers
    def test_add_numbers(self):
        res = calc.add(6,5)
#Checking wether the result is True or False
        self.assertEqual(res, 12)