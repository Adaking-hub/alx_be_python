# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up a SimpleCalculator instance before each test"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various cases"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -7), -12)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)

    def test_subtraction(self):
        """Test the subtract method with various cases"""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)

    def test_multiplication(self):
        """Test the multiply method with various cases"""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_division(self):
        """Test the divide method with various cases"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-9, -3), 3)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_division_by_zero(self):
        """Test dividing by zero returns None"""
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(-10, 0))


if __name__ == "__main__":
    unittest.main()