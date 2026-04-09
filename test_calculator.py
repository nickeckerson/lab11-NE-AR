"""
https://github.com/nickeckerson/lab11-NE-AR.git
Partner 1: Nick Eckerson
Partner 2: Alberto Ramirez-Aguiar
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
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 7), 0)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(-2, 10), -5)
        with self.assertRaises(ZeroDivisionError):
            divide(0, 10)


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
          with self.assertRaises(ZeroDivisionError):
              divide(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        logarithm(10, 5)
        logarithm(100, 10)
        logarithm(25, 5)


    def test_log_invalid_base(self): # 1 assertion
        logarithm(10, 0)

    # ##########################
    
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(-2, 10)
        with self.assertRaises(ValueError):
            logarithm(2, -10)
        with self.assertRaises(ValueError):
            logarithm(0, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(25), 5.0)
        with self.assertRaises(ValueError):
            square_root(-1)

# Do not touch this
if __name__ == "__main__":
    unittest.main()