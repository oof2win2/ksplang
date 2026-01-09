import pytest

from ..constants import MAX_STACK_SIZE, MIN_INT
from ..execute import execute_program
from .ff import FFInstruction


def test_ff_pass():
    instructions = [FFInstruction.notation]
    available_instructions = [FFInstruction]
    stack = [1, 2, 4, 2]
    expected_stack = [1, 2]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_ff_stackfill():
    instructions = [FFInstruction.notation]
    available_instructions = [FFInstruction]
    stack = [1, 4]
    expected_stack = [MIN_INT] * MAX_STACK_SIZE
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_ff_raise():
    instructions = [FFInstruction.notation]
    available_instructions = [FFInstruction]
    stack = [0]
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
