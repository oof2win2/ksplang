import pytest

from ..execute import execute_program
from ..helpers.tetr import tetr
from .tetr import TetrationInstruction


def test_tetr_base_first():
    instructions = [TetrationInstruction.notation]
    available_instructions = [TetrationInstruction]
    stack = [3, 2]
    expected_stack = [tetr(2, 3)]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_tetr_base_second():
    instructions = [TetrationInstruction.notation]
    available_instructions = [TetrationInstruction]
    stack = [4, 2]
    expected_stack = [tetr(2, 4)]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_tetr_zero():
    instructions = [TetrationInstruction.notation]
    available_instructions = [TetrationInstruction]
    stack = [0, 2]
    expected_stack = [1]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )
