import pytest

from ..execute import execute_program
from .plusplus import PlusPlusInstruction


def test_plusplus_once():
    instructions = [PlusPlusInstruction.notation]
    available_instructions = [PlusPlusInstruction]
    stack = [1]
    expected_stack = [2]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_plusplus_empty():
    instructions = [PlusPlusInstruction.notation]
    available_instructions = [PlusPlusInstruction]
    stack = []
    with pytest.raises(ValueError):
        execute_program(instructions, stack, available_instructions)
