
"""
Unit Tests for the Calculator Arithmetic Operations Module.

This module contains comprehensive unit tests for the arithmetic
operations implemented in calculator.core.operations.

The test suite verifies:
    - Correctness of all seven arithmetic operations.
    - Support for integer, floating-point, and complex operands
      where supported by the underlying arithmetic operation.
    - Handling of negative numbers and boundary values.
    - Rejection of invalid operand types.
    - Explicit exclusion of boolean values from numeric operands.
    - Prevention of division by zero.
    - Correct behavior of private validation helper functions.
    - Compliance with the expected function contracts.

Testing Framework:
    unittest

Testing Principles:
    - Arrange, Act, Assert (AAA)
    - Test Isolation
    - Boundary Value Analysis
    - Equivalence Partitioning
    - Negative Testing
    - Exception Testing
    - Parameterized Testing
"""

import unittest

from calculator.core import operations


class TestNumericOperandValidation(unittest.TestCase):
    """Test cases for numeric operand validation."""

    def test_accepts_supported_numeric_types(self):
        """Verify that integers, floats, and complex numbers are accepted."""

        valid_operands = [
            (10, 20),
            (10.5, 20.5),
            (3 + 2j, 4 + 5j),
            (10, 2.5),
            (-10, -2.5),
        ]

        for operands in valid_operands:
            with self.subTest(operands=operands):
                self.assertTrue(
                    operations._validate_numeric_operands(*operands)
                )

    def test_rejects_non_numeric_operands(self):
        """Verify that unsupported operand types are rejected."""

        invalid_operands = [
            ("10", 20),
            (10, "20"),
            (None, 10),
            (10, None),
            ([10], 20),
            ({10: 20}, 30),
            (10, object()),
        ]

        for operands in invalid_operands:
            with self.subTest(operands=operands):
                self.assertFalse(
                    operations._validate_numeric_operands(*operands)
                )

    def test_rejects_boolean_operands(self):
        """Verify that boolean values are not treated as numeric operands."""

        boolean_operands = [
            (True,),
            (False,),
            (10, True),
            (False, 10),
            (True, False),
        ]

        for operands in boolean_operands:
            with self.subTest(operands=operands):
                self.assertFalse(
                    operations._validate_numeric_operands(*operands)
                )

    def test_validates_multiple_operands(self):
        """Verify that every operand is validated independently."""

        self.assertTrue(
            operations._validate_numeric_operands(1, 2, 3, 4.5, 5 + 2j)
        )

        self.assertFalse(
            operations._validate_numeric_operands(1, 2, "3", 4, 5)
        )

    def test_returns_true_when_no_operands_are_provided(self):
        """Verify the all() behavior for an empty operand collection."""

        self.assertTrue(operations._validate_numeric_operands())


class TestNonZeroOperandValidation(unittest.TestCase):
    """Test cases for non-zero operand validation."""

    def test_accepts_non_zero_numeric_values(self):
        """Verify that non-zero integer, float, and complex values are accepted."""

        non_zero_values = [
            1,
            -1,
            0.1,
            -0.1,
            1 + 2j,
            -3j,
        ]

        for value in non_zero_values:
            with self.subTest(value=value):
                self.assertTrue(
                    operations._validate_non_zero_operand(value)
                )

    def test_rejects_zero_values(self):
        """Verify that integer, floating-point, and complex zeros are rejected."""

        zero_values = [
            0,
            0.0,
            -0.0,
            0j,
            complex(0, 0),
        ]

        for value in zero_values:
            with self.subTest(value=value):
                self.assertFalse(
                    operations._validate_non_zero_operand(value)
                )


class TestAddition(unittest.TestCase):
    """Test cases for the addition operation."""

    def test_adds_positive_integers(self):
        """Verify that two positive integers are added correctly."""

        self.assertEqual(operations.add(10, 20), 30)

    def test_adds_negative_integers(self):
        """Verify that two negative integers are added correctly."""

        self.assertEqual(operations.add(-10, -20), -30)

    def test_adds_positive_and_negative_numbers(self):
        """Verify that operands with different signs produce the correct sum."""

        self.assertEqual(operations.add(10, -5), 5)

    def test_adds_floating_point_numbers(self):
        """Verify that floating-point operands produce the correct result."""

        self.assertAlmostEqual(operations.add(2.5, 3.5), 6.0)

    def test_adds_complex_numbers(self):
        """Verify that complex operands are supported by addition."""

        self.assertEqual(
            operations.add(2 + 3j, 4 + 5j),
            6 + 8j,
        )

    def test_adds_zero_to_a_number(self):
        """Verify that adding zero does not change the operand."""

        self.assertEqual(operations.add(100, 0), 100)

    def test_rejects_invalid_operands(self):
        """Verify that invalid operands raise TypeError."""

        invalid_cases = [
            ("10", 20),
            (10, None),
            (True, 10),
            (10, False),
        ]

        for operands in invalid_cases:
            with self.subTest(operands=operands):
                with self.assertRaisesRegex(TypeError, "numeric"):
                    operations.add(*operands)


class TestSubtraction(unittest.TestCase):
    """Test cases for the subtraction operation."""

    def test_subtracts_positive_integers(self):
        """Verify that subtraction of positive integers is correct."""

        self.assertEqual(operations.subtract(20, 10), 10)

    def test_subtracts_negative_integers(self):
        """Verify that subtraction involving negative integers is correct."""

        self.assertEqual(operations.subtract(-10, -5), -5)

    def test_produces_negative_result(self):
        """Verify that subtraction can produce a negative result."""

        self.assertEqual(operations.subtract(5, 10), -5)

    def test_subtracts_floating_point_numbers(self):
        """Verify that floating-point subtraction is accurate."""

        self.assertAlmostEqual(operations.subtract(5.5, 2.5), 3.0)

    def test_subtracts_complex_numbers(self):
        """Verify that complex operands are supported by subtraction."""

        self.assertEqual(
            operations.subtract(5 + 8j, 2 + 3j),
            3 + 5j,
        )

    def test_subtracts_zero(self):
        """Verify that subtracting zero preserves the original value."""

        self.assertEqual(operations.subtract(100, 0), 100)

    def test_rejects_invalid_operands(self):
        """Verify that invalid operands raise TypeError."""

        with self.assertRaises(TypeError):
            operations.subtract("10", 5)


class TestMultiplication(unittest.TestCase):
    """Test cases for the multiplication operation."""

    def test_multiplies_positive_integers(self):
        """Verify that two positive integers are multiplied correctly."""

        self.assertEqual(operations.multiply(5, 4), 20)

    def test_multiplies_negative_integers(self):
        """Verify that multiplication of two negative integers is positive."""

        self.assertEqual(operations.multiply(-5, -4), 20)

    def test_multiplies_numbers_with_different_signs(self):
        """Verify that multiplication of opposite signs is negative."""

        self.assertEqual(operations.multiply(-5, 4), -20)

    def test_multiplies_floating_point_numbers(self):
        """Verify that floating-point multiplication is correct."""

        self.assertAlmostEqual(operations.multiply(2.5, 4.0), 10.0)

    def test_multiplies_complex_numbers(self):
        """Verify that complex operands are supported by multiplication."""

        self.assertEqual(
            operations.multiply(2 + 3j, 4 + 5j),
            -7 + 22j,
        )

    def test_multiplies_by_zero(self):
        """Verify that multiplying any supported number by zero returns zero."""

        self.assertEqual(operations.multiply(100, 0), 0)

    def test_rejects_invalid_operands(self):
        """Verify that invalid operands raise TypeError."""

        with self.assertRaises(TypeError):
            operations.multiply(10, "5")


class TestDivision(unittest.TestCase):
    """Test cases for the true division operation."""

    def test_divides_positive_integers(self):
        """Verify that division of positive integers returns a float."""

        result = operations.divide(10, 2)

        self.assertEqual(result, 5.0)
        self.assertIsInstance(result, float)

    def test_divides_with_fractional_result(self):
        """Verify that division supports non-integer results."""

        self.assertEqual(operations.divide(7, 2), 3.5)

    def test_divides_negative_numbers(self):
        """Verify that division of negative operands is correct."""

        self.assertEqual(operations.divide(-10, 2), -5.0)

    def test_divides_numbers_with_opposite_signs(self):
        """Verify that division of opposite signs produces a negative result."""

        self.assertEqual(operations.divide(10, -2), -5.0)

    def test_divides_floating_point_numbers(self):
        """Verify that floating-point division is correct."""

        self.assertEqual(operations.divide(7.5, 2.5), 3.0)

    def test_divides_complex_numbers(self):
        """Verify that true division supports complex operands."""

        self.assertEqual(
            operations.divide(1 + 2j, 1j),
            2 - 1j,
        )

    def test_raises_zero_division_error_for_zero_divisors(self):
        """Verify that integer, float, and complex zero divisors are rejected."""

        zero_divisors = [0, 0.0, -0.0, 0j, complex(0, 0)]

        for divisor in zero_divisors:
            with self.subTest(divisor=divisor):
                with self.assertRaises(ZeroDivisionError):
                    operations.divide(10, divisor)

    def test_rejects_invalid_operands(self):
        """Verify that invalid operands raise TypeError."""

        with self.assertRaises(TypeError):
            operations.divide("10", 2)


class TestFloorDivision(unittest.TestCase):
    """Test cases for the floor division operation."""

    def test_performs_integer_floor_division(self):
        """Verify that integer floor division returns the correct result."""

        self.assertEqual(operations.floor_divide(10, 3), 3)

    def test_performs_floor_division_with_floats(self):
        """Verify that floating-point floor division is supported."""

        self.assertEqual(operations.floor_divide(10.5, 2.0), 5.0)

    def test_rounds_toward_negative_infinity(self):
        """Verify that negative floor division follows Python semantics."""

        self.assertEqual(operations.floor_divide(-10, 3), -4)

    def test_handles_exact_division(self):
        """Verify that exact floor division produces the expected quotient."""

        self.assertEqual(operations.floor_divide(20, 5), 4)

    def test_raises_zero_division_error_for_zero_divisors(self):
        """Verify that zero integer, float, and complex divisors are rejected."""

        zero_divisors = [0, 0.0, 0j]

        for divisor in zero_divisors:
            with self.subTest(divisor=divisor):
                with self.assertRaises(ZeroDivisionError):
                    operations.floor_divide(10, divisor)

    def test_rejects_invalid_operands(self):
        """Verify that invalid operands raise TypeError."""

        with self.assertRaises(TypeError):
            operations.floor_divide(10, "2")

    def test_rejects_non_zero_complex_operands(self):
        """Verify that Python's unsupported complex floor division raises TypeError."""

        with self.assertRaises(TypeError):
            operations.floor_divide(10, 2 + 1j)


class TestModulo(unittest.TestCase):
    """Test cases for the modulo operation."""

    def test_calculates_integer_remainder(self):
        """Verify that modulo returns the correct integer remainder."""

        self.assertEqual(operations.modulo(10, 3), 1)

    def test_calculates_floating_point_remainder(self):
        """Verify that modulo supports floating-point operands."""

        self.assertAlmostEqual(operations.modulo(10.5, 3.0), 1.5)

    def test_handles_negative_dividend(self):
        """Verify that the remainder follows Python's modulo semantics."""

        self.assertEqual(operations.modulo(-10, 3), 2)

    def test_handles_negative_divisor(self):
        """Verify that the remainder has the sign of the divisor."""

        self.assertEqual(operations.modulo(10, -3), -2)

    def test_handles_exact_division(self):
        """Verify that modulo returns zero for exactly divisible operands."""

        self.assertEqual(operations.modulo(20, 5), 0)

    def test_raises_zero_division_error_for_zero_divisors(self):
        """Verify that zero integer, float, and complex divisors are rejected."""

        zero_divisors = [0, 0.0, 0j]

        for divisor in zero_divisors:
            with self.subTest(divisor=divisor):
                with self.assertRaises(ZeroDivisionError):
                    operations.modulo(10, divisor)

    def test_rejects_invalid_operands(self):
        """Verify that invalid operands raise TypeError."""

        with self.assertRaises(TypeError):
            operations.modulo("10", 3)

    def test_rejects_non_zero_complex_operands(self):
        """Verify that Python's unsupported complex modulo raises TypeError."""

        with self.assertRaises(TypeError):
            operations.modulo(10, 2 + 1j)


class TestPower(unittest.TestCase):
    """Test cases for the exponentiation operation."""

    def test_calculates_positive_integer_exponentiation(self):
        """Verify that positive integer exponentiation is correct."""

        self.assertEqual(operations.power(2, 3), 8)

    def test_calculates_zero_exponent(self):
        """Verify that a non-zero base raised to zero equals one."""

        self.assertEqual(operations.power(10, 0), 1)

    def test_calculates_negative_exponent(self):
        """Verify that negative exponents produce reciprocal results."""

        self.assertEqual(operations.power(2, -2), 0.25)

    def test_calculates_fractional_exponent(self):
        """Verify that fractional exponents are supported."""

        self.assertEqual(operations.power(9, 0.5), 3.0)

    def test_calculates_negative_base_with_integer_exponent(self):
        """Verify that negative bases with integer exponents are supported."""

        self.assertEqual(operations.power(-2, 3), -8)

    def test_calculates_complex_exponentiation(self):
        """Verify that exponentiation supports complex operands."""

        self.assertEqual(operations.power(1 + 1j, 2), 2j)

    def test_raises_zero_division_error_for_zero_base_and_negative_exponent(self):
        """Verify that zero raised to a negative power raises ZeroDivisionError."""

        with self.assertRaises(ZeroDivisionError):
            operations.power(0, -1)

    def test_rejects_invalid_operands(self):
        """Verify that invalid operands raise TypeError."""

        with self.assertRaises(TypeError):
            operations.power(2, "3")


if __name__ == "__main__":
    unittest.main(verbosity=2, descriptions=True)
