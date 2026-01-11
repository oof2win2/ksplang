import pytest
from .rem import RemInstruction


@pytest.mark.parametrize(
    "dividend,divisor,expected",
    [
        (3, 1, 1),
        (-3, 1, 1),
        (3, -1, -1),
        (-3, -1, -1),
    ],
)
def test_rem(dividend, divisor, expected, execute_single_instruction):
    assert execute_single_instruction(RemInstruction, [dividend, divisor]) == [expected]


def test_rem_insufficient_elements_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(RemInstruction, [10])
