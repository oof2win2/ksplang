import pytest
from ...execute import execute_program
from .lswap import LSwapInstruction


def test_lswap_swaps_first_and_last(execute_single_instruction):
    assert execute_single_instruction(LSwapInstruction, [1, 2, 3, 4]) == [4, 2, 3, 1]


def test_lswap_twice_returns_original():
    instructions = [LSwapInstruction.notation, LSwapInstruction.notation]
    assert execute_program(instructions, [1, 2, 3, 4], [LSwapInstruction]) == [
        1,
        2,
        3,
        4,
    ]


def test_lswap_empty_stack_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(LSwapInstruction, [])
