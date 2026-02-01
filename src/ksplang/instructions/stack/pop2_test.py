import pytest

from .pop2 import Pop2Instruction


def test_pop2_removes_second_element(execute_single_instruction):
    assert execute_single_instruction(Pop2Instruction, [1, 2, 3]) == [1, 3]


def test_pop2_multiple_removes_many_elements(execute_multiple_instructions):
    instructions = [Pop2Instruction.id] * 5
    assert execute_multiple_instructions(
        [Pop2Instruction], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], instructions
    ) == [1, 2, 3, 4, 10]


def test_pop2_empty_stack_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(Pop2Instruction, [])
