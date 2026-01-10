import pytest
from ...execute import execute_program
from .pop import PopInstruction


def test_pop_removes_top_element(execute_single_instruction):
    assert execute_single_instruction(PopInstruction, [1, 2, 3]) == [1, 2]


def test_pop_multiple_removes_many_elements():
    instructions = [PopInstruction.notation] * 5
    assert execute_program(
        instructions, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [PopInstruction]
    ) == [1, 2, 3, 4, 5]


def test_pop_empty_stack_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(PopInstruction, [])
