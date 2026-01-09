import pytest

from ..execute import execute_program
from .pop2 import Pop2Instruction


def test_pop2_once():
    instructions = [Pop2Instruction.notation]
    available_instructions = [Pop2Instruction]
    stack = [1, 2, 3]
    expected_stack = [1, 3]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_pop3_multiple():
    instructions = [Pop2Instruction.notation] * 5
    available_instructions = [Pop2Instruction]
    stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_stack = [1, 2, 3, 4, 10]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_pop_empty():
    instructions = [Pop2Instruction.notation]
    available_instructions = [Pop2Instruction]
    stack = []
    # expect to throw an error, as negative repetitions throw
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
