import pytest
from .euclid_modulo import EuclidianModuloInstruction


@pytest.mark.parametrize(
    "dividend,divisor,expected",
    [
        (3, 1, 1),
        (-3, 1, 1),
        (3, -1, 2),
        (-3, -1, 2),
    ],
)
def test_euclid_modulo(dividend, divisor, expected, execute_single_instruction):
    assert execute_single_instruction(
        EuclidianModuloInstruction, [dividend, divisor]
    ) == [expected]


def test_euclid_modulo_insufficient_elements_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(EuclidianModuloInstruction, [10])
