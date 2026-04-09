"""https://github.com/nickeckerson/lab11-NE-AR.git
Partner 1: Nick Eckerson
Partner 2: Alberto Ramirez-Aguiar"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    else: return a / b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm input")
    return math.log(b, a)

def exp(a, b):
    return a ** b