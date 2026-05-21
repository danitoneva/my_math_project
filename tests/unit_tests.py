import unittest
import src.my_math as my_math

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(my_math.add(1, 2), 3)
        self.assertEqual(my_math.add(-1, -1), -2)
        self.assertEqual(my_math.add(-1, 2), 1)

    def test_substract(self):
        self.assertEqual(my_math.subtract(2, 1), 1)
        self.assertEqual(my_math.subtract(1, 2), -1)
        self.assertEqual(my_math.subtract(0, 2), -2)

    def test_multiply(self):
        self.assertEqual(my_math.multiply(2, 3), 6)
        self.assertEqual(my_math.multiply(-2, -2), 4)
        self.assertEqual(my_math.multiply(0, 4), 0)

    def test_divide(self):
        self.assertEqual(my_math.divide(6, 2), 3)
        self.assertEqual(my_math.divide(5, 2), 2.5)

if __name__ == '__main__':
    unittest.main()