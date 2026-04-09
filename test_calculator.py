"""
Partner 1: Nick Eckerson
Partner 2: Alberto Ramirez-Aguiar
https://github.com/nickeckerson/lab11-NE-AR.git
"""

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        add(4, 3)
        add(5, 6)
        add(7, 102)


    def test_subtract(self): # 3 assertions
        subtract(105, 102)
        subtract(4, 2)
        subtract(248564, 248563)


    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
          with self.assertRaises(ZeroDivisionError):
              div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        logarithm(10, 5)
        logarithm(100, 10)
        logarithm(25, 5)


    def test_log_invalid_base(self): # 1 assertion
        logarithm(10, 0)

    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()