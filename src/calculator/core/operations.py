
"""
Mathematical Operations Module.

This module provides a collection of independent, reusable functions
for performing fundamental arithmetic operations.

Each function accepts numeric operands and returns the result of
the corresponding mathematical operation.

The module is intentionally independent of user input, output,
application workflows, and presentation logic.

Functions:
    add: Calculate the sum of two numbers.
    subtract: Calculate the difference between two numbers.
    multiply: Calculate the product of two numbers.
    divide: Calculate the quotient of two numbers.
    floor_divide: Calculate the floor division of two numbers.
    modulo: Calculate the remainder of a division.
    power: Calculate the result of raising a number to a power.
"""


def _validate_non_zero_operand(operand: int | float | complex) -> bool:
    """
    Validate that the given numeric operand is not equal to zero.

    Args:
        operand: The numeric value to validate.

    Returns:
        True if the operand is non-zero; otherwise, False.

    Example:
        >>> _validate_non_zero_operand(10)
        True
        >>> _validate_non_zero_operand(0.0)
        False
        >>> _validate_non_zero_operand(0j)
        False
    """
    return operand != 0


def _validate_numeric_operands(*operands: object) -> bool:
    """
    Validate that all provided operands are numeric values.

    This function checks whether every operand belongs to a supported
    numeric type. Boolean values are explicitly excluded because bool
    is a subclass of int in Python.

    Args:
        *operands: A variable number of operands to validate.

    Returns:
        True if all operands are numeric; otherwise, False.

    Example:
        >>> _validate_numeric_operands(10, 20, 3.5)
        True
        >>> _validate_numeric_operands(10, "20", 3.5)
        False
        >>> _validate_numeric_operands(True, 10)
        False
    """
    return all(
        isinstance(operand, (int, float, complex)
                   ) and not isinstance(operand, bool)
        for operand in operands
    )


def add(first_operand: float, second_operand: float) -> float:
    """
    Calculate the sum of two numeric operands.

    Args:
        first_operand: The first numeric operand.
        second_operand: The second numeric operand.

    Returns:
        The arithmetic sum of the two operands.

    Raises:
        TypeError: If either operand is not a supported numeric type.

    Example:
        >>> add(10, 5)
        15
        >>> add(2.5, 3.5)
        6.0
    """
    if not _validate_numeric_operands(first_operand, second_operand):
        raise TypeError("Both operands must be numeric values.")

    return first_operand + second_operand


def subtract(first_operand: float, second_operand: float) -> float:
    """
    Calculate the difference between two numeric operands.

    The second operand is subtracted from the first operand.

    Args:
        first_operand: The minuend.
        second_operand: The subtrahend.

    Returns:
        The arithmetic difference between the two operands.

    Raises:
        TypeError: If either operand is not a supported numeric type.

    Example:
        >>> subtract(10, 5)
        5
        >>> subtract(5, 10)
        -5
    """
    if not _validate_numeric_operands(first_operand, second_operand):
        raise TypeError("Both operands must be numeric values.")

    return first_operand - second_operand


def multiply(first_operand: float, second_operand: float) -> float:
    """
    Calculate the product of two numeric operands.

    Args:
        first_operand: The first numeric operand.
        second_operand: The second numeric operand.

    Returns:
        The arithmetic product of the two operands.

    Raises:
        TypeError: If either operand is not a supported numeric type.

    Example:
        >>> multiply(4, 5)
        20
        >>> multiply(2.5, 4)
        10.0
    """
    if not _validate_numeric_operands(first_operand, second_operand):
        raise TypeError("Both operands must be numeric values.")

    return first_operand * second_operand


def divide(first_operand: float, second_operand: float) -> float:
    """
    Perform true division between two numeric operands.

    Args:
        first_operand: The dividend.
        second_operand: The divisor.

    Returns:
        The quotient of the division.

    Raises:
        ZeroDivisionError: If the second operand is zero.
        TypeError: If either operand is not a supported numeric type.

    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if not _validate_numeric_operands(first_operand, second_operand):
        raise TypeError("Both operands must be numeric values.")
    
    if not _validate_non_zero_operand(second_operand):
        raise ZeroDivisionError("Division by zero is not allowed.")

    return first_operand / second_operand


def floor_divide(first_operand: float, second_operand: float) -> float:
    """
    Perform floor division between two numeric operands.

    The result is rounded down toward negative infinity.

    Args:
        first_operand: The dividend.
        second_operand: The divisor.

    Returns:
        The floor division result.

    Raises:
        ZeroDivisionError: If the second operand is zero.
        TypeError: If either operand is not a supported numeric type.

    Example:
        >>> floor_divide(10, 3)
        3
        >>> floor_divide(-10, 3)
        -4
    """
    if not _validate_numeric_operands(first_operand, second_operand):
        raise TypeError("Both operands must be numeric values.")
    
    if not _validate_non_zero_operand(second_operand):
        raise ZeroDivisionError("Division by zero is not allowed.")

    return first_operand // second_operand


def modulo(first_operand: float, second_operand: float) -> float:
    """
    Calculate the remainder of dividing two numeric operands.

    The remainder follows Python's modulo semantics, where the
    result has the same sign as the divisor (unless the result is zero).

    Args:
        first_operand: The dividend.
        second_operand: The divisor.

    Returns:
        The remainder of the division.

    Raises:
        ZeroDivisionError: If the second operand is zero.
        TypeError: If either operand is not a supported numeric type.

    Example:
        >>> modulo(10, 3)
        1
        >>> modulo(-10, 3)
        2
    """
    if not _validate_numeric_operands(first_operand, second_operand):
        raise TypeError("Both operands must be numeric values.")
    
    if not _validate_non_zero_operand(second_operand):
        raise ZeroDivisionError("Division by zero is not allowed.")

    return first_operand % second_operand


def power(first_operand: float, second_operand: float) -> float:
    """
    Raise the first numeric operand to the power of the second operand.

    Args:
        first_operand: The base.
        second_operand: The exponent.

    Returns:
        The result of exponentiation.

    Raises:
        TypeError: If either operand is not a supported numeric type.
        ZeroDivisionError: If zero is raised to a negative power.
        ValueError: If the operation produces an invalid mathematical result.

    Example:
        >>> power(2, 3)
        8
        >>> power(5, 2)
        25
        >>> power(9, 0.5)
        3.0
    """
    if not _validate_numeric_operands(first_operand, second_operand):
        raise TypeError("Both operands must be numeric values.")

    return first_operand ** second_operand
