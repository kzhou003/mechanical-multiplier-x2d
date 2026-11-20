import unittest

from simulations.arithmetic_model import (
    add_decimal_digits,
    multiply_by_repeated_addition,
)


class ArithmeticModelTests(unittest.TestCase):
    def test_decimal_carry(self):
        self.assertEqual(add_decimal_digits(9, 1), 10)
        self.assertEqual(add_decimal_digits(99, 1), 100)
        self.assertEqual(add_decimal_digits(999, 1), 1000)

    def test_multi_digit_addition(self):
        self.assertEqual(add_decimal_digits(123, 456), 579)
        self.assertEqual(add_decimal_digits(987, 654), 1641)

    def test_repeated_addition_multiplication(self):
        self.assertEqual(multiply_by_repeated_addition(7, 8), 56)
        self.assertEqual(multiply_by_repeated_addition(12, 13), 156)
        self.assertEqual(multiply_by_repeated_addition(99, 99), 9801)

    def test_zero_and_one(self):
        self.assertEqual(multiply_by_repeated_addition(0, 123), 0)
        self.assertEqual(multiply_by_repeated_addition(123, 0), 0)
        self.assertEqual(multiply_by_repeated_addition(123, 1), 123)

    def test_negative_inputs_rejected(self):
        with self.assertRaises(ValueError):
            multiply_by_repeated_addition(-1, 2)


if __name__ == "__main__":
    unittest.main()
