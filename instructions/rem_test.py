import pytest

from ..execute import execute_program
from .rem import RemInstruction


def test_rem_mod_one():
    instructions = [RemInstruction.notation]
    available_instructions = [RemInstruction]
    stack = [3, 1]
    expected_stack = [1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_rem_mod_two():
    instructions = [RemInstruction.notation]
    available_instructions = [RemInstruction]
    stack = [-3, 1]
    expected_stack = [1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_rem_mod_three():
    instructions = [RemInstruction.notation]
    available_instructions = [RemInstruction]
    stack = [3, -1]
    expected_stack = [-1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_rem_mod_four():
    instructions = [RemInstruction.notation]
    available_instructions = [RemInstruction]
    stack = [-3, -1]
    expected_stack = [-1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_rem_raise():
    instructions = [RemInstruction.notation]
    available_instructions = [RemInstruction]
    stack = [10]
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
