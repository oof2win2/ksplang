import pytest
from .plusplus import PlusPlusInstruction


def test_plusplus_increments_value(execute_single_instruction):
    assert execute_single_instruction(PlusPlusInstruction, [1]) == [2]


def test_plusplus_empty_stack_raises_error(execute_single_instruction):
    with pytest.raises(ValueError):
        execute_single_instruction(PlusPlusInstruction, [])
