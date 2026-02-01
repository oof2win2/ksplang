import pytest

from ...constants import MAX_STACK_SIZE, MIN_INT
from .ff import FFInstruction


def test_ff_filters_excessive_stack(execute_single_instruction):
    assert execute_single_instruction(FFInstruction, [1, 2, 4, 2]) == [1, 2]


def test_ff_fills_stack_to_max_size(execute_single_instruction):
    assert (
        execute_single_instruction(FFInstruction, [1, 4]) == [MIN_INT] * MAX_STACK_SIZE
    )


def test_ff_raises_error_on_zero_limit(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(FFInstruction, [0])
