
"""
Core Module - Arithmetic Operations.

This package provides reusable arithmetic operations and exposes
them through a centralized public interface.

The package is independent of user interaction, presentation logic,
and application workflows.

Public API:
    add: Perform addition.
    subtract: Perform subtraction.
    multiply: Perform multiplication.
    divide: Perform true division.
    floor_divide: Perform floor division.
    modulo: Calculate the division remainder.
    power: Perform exponentiation.

Example:
    >>> from calculator.core import add
    >>> add(10, 20)
    30
"""

from calculator.core.operations import (
    add,
    subtract,
    multiply,
    divide,
    floor_divide,
    modulo,
    power,
)

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "floor_divide",
    "modulo",
    "power",
]
