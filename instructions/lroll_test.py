import pytest

from ..execute import execute_program
from .lroll import LRollInstruction


def test_lroll_first():
    instructions = [LRollInstruction.notation]
    available_instructions = [LRollInstruction]
    stack = [1, 2, 3, 4, 1, 4]
    expected_stack = [4, 1, 2, 3]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_lroll_second():
    instructions = [LRollInstruction.notation]
    available_instructions = [LRollInstruction]
    stack = [1, 2, 3, 4, -1, 4]
    expected_stack = [2, 3, 4, 1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_lroll_third():
    instructions = [LRollInstruction.notation]
    available_instructions = [LRollInstruction]
    stack = [0, 1, 2, 3, 4, 2, 4]
    expected_stack = [0, 3, 4, 1, 2]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_lroll_raise():
    instructions = [LRollInstruction.notation]
    available_instructions = [LRollInstruction]
    stack = [0]
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
