""" 
Sample test
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """ Test the calc moduler. """
    
    def test_add_numbers(self):
        res = calc.add(5, 6)
        self.assertEqual(res, 11);
        
    def test_subtract_numbers(self):
        """ Test Subtracting Numbers """
        res = calc.subtract(15, 10)
        
        self.assertEqual(res, 5)
        