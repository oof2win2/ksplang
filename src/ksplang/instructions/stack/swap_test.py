import pytest
from .swap import SwapInstruction


def test_swap_swaps_with_nth_element(execute_single_instruction):
    assert execute_single_instruction(SwapInstruction, [1, 2, 3, 4, 5, 6, 7, 8, 3]) == [
        1,
        2,
        3,
        8,
        5,
        6,
        7,
        4,
    ]


def test_swap_negative_index_raises_error(execute_single_instruction):
    with pytest.raises(IndexError):
        execute_single_instruction(SwapInstruction, [1, 2, 3, 4, 5, 6, 7, 8, -1])


def test_swap_out_of_bounds_raises_error(execute_single_instruction):
    stack = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    with pytest.raises(IndexError):
        execute_single_instruction(SwapInstruction, stack)
