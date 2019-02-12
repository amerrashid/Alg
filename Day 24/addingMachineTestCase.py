import unittest

from .addingMachine import add

class Tests(unittest.TestCase):

    def test_add_integers(self):

        num1 = 2
        num2 = 3
        expectedResult = 5

        result = add(num1, num2)

        self.assertEqual(expectedResult, result)

    def test_add_floats(self):
        num1 = 2.0
        num2 = 3.0
        expectedResult = 5.0

        result = add(num1, num2)

        self.assertEqual(expectedResult, result)

