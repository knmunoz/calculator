import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2,3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(12,8), 4)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4,5), 20)

    def test_divide(self):
        self.assertEqual(calculator.divide(21,7), 3)

if __name__ == "__main__":
    unittest.main(verbosity=2)