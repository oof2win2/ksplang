import pytest
from .praise import PraiseInstruction


PRAISE_OUTPUT = [77, 225, 109, 32, 114, 225, 100, 32, 75, 83, 80]


def test_praise_pushes_output_once(execute_single_instruction):
    assert execute_single_instruction(PraiseInstruction, [1]) == PRAISE_OUTPUT


def test_praise_zero_pushes_nothing(execute_single_instruction):
    assert execute_single_instruction(PraiseInstruction, [0]) == []


def test_praise_multiple_pushes_repeated_output(execute_single_instruction):
    assert execute_single_instruction(PraiseInstruction, [10]) == PRAISE_OUTPUT * 10


def test_praise_negative_count_raises_error(execute_single_instruction):
    with pytest.raises(ValueError):
        execute_single_instruction(PraiseInstruction, [-1])


def test_praise_empty_stack_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(PraiseInstruction, [])
