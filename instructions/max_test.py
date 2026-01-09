import pytest

from ..execute import execute_program
from .max import MaxInstruction


def test_max():
    instructions = [MaxInstruction.notation]
    available_instructions = [MaxInstruction]
    stack = [4, 2]
    expected_stack = [4]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_plusplus_empty():
    instructions = [MaxInstruction.notation]
    available_instructions = [MaxInstruction]
    stack = []
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
