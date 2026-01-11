import pytest

from .lroll import LRollInstruction


def test_lroll_rotates_forward(execute_single_instruction):
    assert execute_single_instruction(LRollInstruction, [1, 2, 3, 4, 1, 4]) == [
        4,
        1,
        2,
        3,
    ]


def test_lroll_rotates_backward(execute_single_instruction):
    assert execute_single_instruction(LRollInstruction, [1, 2, 3, 4, -1, 4]) == [
        2,
        3,
        4,
        1,
    ]


def test_lroll_with_multiple_elements(execute_single_instruction):
    assert execute_single_instruction(LRollInstruction, [0, 1, 2, 3, 4, 2, 4]) == [
        0,
        3,
        4,
        1,
        2,
    ]


def test_lroll_insufficient_elements_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(LRollInstruction, [0])
