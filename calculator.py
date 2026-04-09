# https://github.com/nickeckerson/lab11-NE-AR
# Nicholas Eckerson
# Alberto Ramirez

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


def multiply(a, b):
    return a * b


def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm input")
    return math.log(b, a)


def exponent(a, b):
    return a ** b


<<<<<<< HEAD
=======
One function per operation, in order.

Partner 1: Nick Eckerson
Partner 2: Alberto Ramirez-Aguiar
https://github.com/nickeckerson/lab11-NE-AR.git


"""
# First example
import math
def add(a, b):
    return a + b
>>>>>>> 9f1f860157bca0f0f51846bbe8d9f683cefc680c

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    else: return b / a

def log(a, b):
    return math.log(b, a)

def exp(a, b):
    return a ** b

