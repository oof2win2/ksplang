import pytest

from ..execute import execute_program
from .lswap import LSwapInstruction


def test_lswap_once():
    instructions = [LSwapInstruction.notation]
    available_instructions = [LSwapInstruction]
    stack = [1, 2, 3, 4]
    expected_stack = [4, 2, 3, 1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_lswap_twice():
    instructions = [LSwapInstruction.notation, LSwapInstruction.notation]
    available_instructions = [LSwapInstruction]
    stack = [1, 2, 3, 4]
    expected_stack = [1, 2, 3, 4]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_lswap_empty():
    instructions = [LSwapInstruction.notation]
    available_instructions = [LSwapInstruction]
    stack = []
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
