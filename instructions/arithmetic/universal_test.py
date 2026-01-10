import pytest
from .universal import UniversalMathInstruction


def test_sum(execute_single_instruction):
    assert execute_single_instruction(UniversalMathInstruction, [1, 2, 0]) == [3]


def test_abs_difference(execute_single_instruction):
    assert execute_single_instruction(UniversalMathInstruction, [5, 8, 1]) == [3]


def test_multiply(execute_single_instruction):
    assert execute_single_instruction(UniversalMathInstruction, [3, 8, 2]) == [24]


def test_divide(execute_single_instruction):
    assert execute_single_instruction(UniversalMathInstruction, [2, 6, 3]) == [3]


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (4, 10, 2),
        (10, 4, 4),
    ],
)
def test_modulo(a, b, expected, execute_single_instruction):
    assert execute_single_instruction(UniversalMathInstruction, [a, b, 3]) == [expected]


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (-3, 1, 1),
        (3, -1, -1),
        (-3, -1, -1),
    ],
)
def test_modulo_c_behavior(a, b, expected, execute_single_instruction):
    assert execute_single_instruction(UniversalMathInstruction, [a, b, 3]) == [expected]


def test_invalid_operation_raises_error(execute_single_instruction):
    with pytest.raises(ValueError):
        execute_single_instruction(UniversalMathInstruction, [10])
