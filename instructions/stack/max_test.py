import pytest
from .max import MaxInstruction


def test_max_returns_greater_value(execute_single_instruction):
    assert execute_single_instruction(MaxInstruction, [4, 2]) == [4]


def test_max_empty_stack_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(MaxInstruction, [])
