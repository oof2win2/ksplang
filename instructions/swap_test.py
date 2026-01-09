import pytest

from ..execute import execute_program
from .swap import SwapInstruction


def test_swap_example():
    instructions = [SwapInstruction.notation]
    available_instructions = [SwapInstruction]
    stack = [1, 2, 3, 4, 5, 6, 7, 8, 3]
    expected_stack = [1, 2, 3, 8, 5, 6, 7, 4]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_swap_negative():
    instructions = [SwapInstruction.notation]
    available_instructions = [SwapInstruction]
    stack = [1, 2, 3, 4, 5, 6, 7, 8, -1]
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)


def test_swap_large():
    instructions = [SwapInstruction.notation]
    available_instructions = [SwapInstruction]
    stack = [1, 2, 3, 4, 5, 6, 7, 8]
    stack.append(len(stack) + 1)  # this should be OOB
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
