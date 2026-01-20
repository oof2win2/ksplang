import pytest

from .sum import SumInstruction


def test_sum(execute_single_instruction):
    numbers = [x for x in range(10_000)]
    total = sum(numbers)
    assert execute_single_instruction(SumInstruction, numbers) == [total]


def test_sum_none(execute_single_instruction):
    assert execute_single_instruction(SumInstruction, []) == [0]


def test_sum_overflow(execute_single_instruction):
    numbers = [2**63 - 1, 5]
    with pytest.raises(ValueError):
        execute_single_instruction(SumInstruction, numbers)
