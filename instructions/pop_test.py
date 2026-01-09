
import pytest

from ..execute import execute_program
from .pop import PopInstruction


def test_pop_once():
    instructions = [PopInstruction.notation]
    available_instructions = [PopInstruction]
    stack = [1, 2, 3]
    expected_stack = [1, 2]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_pop_multiple():
    instructions = [PopInstruction.notation] * 5
    available_instructions = [PopInstruction]
    stack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected_stack = [1, 2, 3, 4, 5]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )

def test_pop_empty():
    instructions = [PopInstruction.notation]
    available_instructions = [PopInstruction]
    stack = []
    # expect to throw an error, as negative repetitions throw
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
