import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add1(self):
        self.assertEqual(self.calc.add(9, 10), 19)

    def test_add2(self):
        self.assertEqual(self.calc.add(20, 30), 50)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(-3, -7), 4)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(6, 4), 24)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-5, 3), -15)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(20, 4), 5.0)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(7, 1), 7)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(15, 4), 3)

if __name__ == '__main__':
    unittest.main()