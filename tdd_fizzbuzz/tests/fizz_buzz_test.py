import unittest
from src.fizz_buzz import *

class FizzBuzzTest(unittest.TestCase):


    def test_returns_int_as_str(self): 
        self.assertEqual("1",fizz_buzz(1))

    def test_divisible_by_3(self):
        self.assertEqual("Fizz",fizz_buzz(3))

    def test_divisible_by_5(self):
        self.assertEqual("Buzz",fizz_buzz(5))

    def test_divisible_by_15(self):
        self.assertEqual("Fizz Buzz",fizz_buzz(15))

    def test_not_an_int(self):
        self.assertEqual("This is not a number!!!",fizz_buzz("Rubber Duck"))

