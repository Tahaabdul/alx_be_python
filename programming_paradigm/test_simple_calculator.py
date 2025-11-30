import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- Tests for add() ---
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -4), -6)

    def test_add_mixed_numbers(self):
        self.assertEqual(self.calc.add(-1, 5), 4)

    # --- Tests for subtract() ---
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(3, 10), -7)

    # --- Tests for multiply() ---
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 6), 24)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-3, -7), 21)

    # --- Tests for divide() ---
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(20, 5), 4)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-15, 3), -5)

    def test_divide_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))


if __name__ == "__main__":
    unittest.main()
