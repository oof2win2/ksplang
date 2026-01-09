import pytest

from ..execute import execute_program
from .praise import PraiseInstruction


def test_praise_once():
    instructions = [PraiseInstruction.notation]
    available_instructions = [PraiseInstruction]
    stack = [1]
    expected_stack = [77, 225, 109, 32, 114, 225, 100, 32, 75, 83, 80]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_praise_zero():
    instructions = [PraiseInstruction.notation]
    available_instructions = [PraiseInstruction]
    stack = [0]
    expected_stack = []
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_praise_many():
    instructions = [PraiseInstruction.notation]
    available_instructions = [PraiseInstruction]
    stack = [10]
    expected_stack = [77, 225, 109, 32, 114, 225, 100, 32, 75, 83, 80] * 10
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_praise_negative():
    instructions = [PraiseInstruction.notation]
    available_instructions = [PraiseInstruction]
    stack = [-1]
    # expect to throw an error, as negative repetitions throw
    with pytest.raises(ValueError):
        execute_program(instructions, stack, available_instructions)

def test_praise_empty():
    instructions = [PraiseInstruction.notation]
    available_instructions = [PraiseInstruction]
    stack = []
    # expect to throw an error
    with pytest.raises(IndexError):
        execute_program(instructions, stack, available_instructions)
