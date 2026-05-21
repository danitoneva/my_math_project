"""
Tests for my math module
"""


import unittest
from src.my_math import MathModule

class TestMyMath(unittest.TestCase):
    """ Class test MyMath"""

    def test_add_two_positive_numbers(self):
        expected_result = 4
        actual_result = MathModule.add_two_numbers(number1 = 2, number2 = 2)
        self.assertEqual(expected_result, actual_result)

    def test_add_two_negavive_numbers(self):
        expected_result = -4
        actual_result = MathModule.add_two_numbers(number1 = -2, number2 = -2)
        self.assertEqual(expected_result, actual_result)

    def test_add_positive_and_negative_numbers(self):
        expected_result = 0
        actual_result = MathModule.add_two_numbers(number1 = 2, number2 = -2)
        self.assertEqual(expected_result, actual_result)

    def test_substract_two_positive_numbers(self):
        expected_result = 2
        actual_result = MathModule.subtract_two_numbers(number1 = 4, number2 = 2)
        self.assertEqual(expected_result, actual_result)

    def test_substract_two_negavive_numbers(self):
        expected_result = -2
        actual_result = MathModule.subtract_two_numbers(number1 = -4, number2 = -2)
        self.assertEqual(expected_result, actual_result)

    def test_substract_positive_and_negative_numbers(self):
        expected_result = 4
        actual_result = MathModule.subtract_two_numbers(number1 = 2, number2 = -2)
        self.assertEqual(expected_result, actual_result)

    def test_multiply_two_positive_numbers(self):
        expected_result = 6
        actual_result = MathModule.multiply_two_numbers(number1 = 2, number2 = 3)
        self.assertEqual(expected_result, actual_result)

    def test_multiply_two_negavive_numbers(self):
        expected_result = 6
        actual_result = MathModule.multiply_two_numbers(number1 = -2, number2 = -3)
        self.assertEqual(expected_result, actual_result)

    def test_multiply_positive_and_negative_numbers(self):
        expected_result = -6
        actual_result = MathModule.multiply_two_numbers(number1 = 2, number2 = -3)
        self.assertEqual(expected_result, actual_result)

    def test_divide_two_positive_numbers(self):
        expected_result = 3
        actual_result = MathModule.divide_two_numbers(number1 = 6, number2 = 2)
        self.assertEqual(expected_result, actual_result)

    def test_divide_two_negavive_numbers(self):
        expected_result = 3
        actual_result = MathModule.divide_two_numbers(number1 = -6, number2 = -2)
        self.assertEqual(expected_result, actual_result)

    def test_divide_positive_and_negative_numbers(self):
        expected_result = -3
        actual_result = MathModule.divide_two_numbers(number1 = 6, number2 = -2)
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
   unittest.main()