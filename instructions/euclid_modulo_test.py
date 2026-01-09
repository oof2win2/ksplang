import pytest

from ..execute import execute_program
from .euclid_modulo import EuclidianModuloInstruction


def test_euclid_mod_one():
    instructions = [EuclidianModuloInstruction.notation]
    available_instructions = [EuclidianModuloInstruction]
    stack = [3, 1]
    expected_stack = [1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_euclid_mod_two():
    instructions = [EuclidianModuloInstruction.notation]
    available_instructions = [EuclidianModuloInstruction]
    stack = [-3, 1]
    expected_stack = [1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_euclid_mod_three():
    instructions = [EuclidianModuloInstruction.notation]
    available_instructions = [EuclidianModuloInstruction]
    stack = [3, -1]
    expected_stack = [2]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_euclid_mod_four():
    instructions = [EuclidianModuloInstruction.notation]
    available_instructions = [EuclidianModuloInstruction]
    stack = [-3, -1]
    expected_stack = [2]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_euclid_mod_raise():
    instructions = [EuclidianModuloInstruction.notation]
    available_instructions = [EuclidianModuloInstruction]
    stack = [10]
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
