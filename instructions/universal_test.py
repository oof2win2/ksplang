import pytest

from ..execute import execute_program
from .universal import UniversalMathInstruction


def test_u_sum():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [1, 2, 0]
    expected_stack = [3]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_u_abs():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [5, 8, 1]
    expected_stack = [3]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_u_multiply():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [3, 8, 2]
    expected_stack = [24]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_u_div():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [2, 6, 3]
    expected_stack = [3]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_u_mod_largerfirst():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [4, 10, 3]
    expected_stack = [2]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_u_mod_smallerfirst():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [10, 4, 3]
    expected_stack = [4]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


# we must assert it behaves like C modulo, not python modulo
def test_u_mod_negative_one():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [-3, 1, 3]
    expected_stack = [1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_u_mod_negative_two():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [3, -1, 3]
    expected_stack = [-1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_u_mod_negative_three():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [-3, -1, 3]
    expected_stack = [-1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_u_raise():
    instructions = [UniversalMathInstruction.notation]
    available_instructions = [UniversalMathInstruction]
    stack = [10]
    with pytest.raises(ValueError):
        execute_program(instructions, stack, available_instructions)
