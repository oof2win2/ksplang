import pytest

from ksplang.instructions.arithmetic.plusplus import PlusPlusInstruction
from ksplang.instructions.control.goto import GotoInstruction
from ksplang.instructions.extra.nop import NopInstruction
from ksplang.instructions.stack.pop import PopInstruction

from .rev import ReverseInstruction


def test_rev_docs(execute_multiple_instructions):
    # rev 2 forward, stack is rotated to [4, 3, 2, 1], pop twice, return to nop
    assert execute_multiple_instructions(
        [ReverseInstruction, PlusPlusInstruction, PopInstruction],
        [1, 2, 3, 4, 2, 0],
        [
            ReverseInstruction.notation,
            PlusPlusInstruction.notation,
            PopInstruction.notation,
            PopInstruction.notation,
        ],
    ) == [3, 3]


def test_rev_one(execute_multiple_instructions):
    # assert it skips one plusplus
    assert execute_multiple_instructions(
        [ReverseInstruction, NopInstruction],
        [1, 2, 3, 4, 0, 0],
        [
            ReverseInstruction.notation,
            NopInstruction.notation,
        ],
    ) == [1, 2, 3, 4]


def test_rev_two(execute_multiple_instructions):
    # Essentially a nop with a quadratic equation (x = -2 and x = 0)
    assert execute_multiple_instructions(
        [ReverseInstruction, NopInstruction],
        [1, 2, 3, 4, 0, 2, 1],
        [
            ReverseInstruction.notation,
            NopInstruction.notation,
        ],
    ) == [1, 2, 3, 4]


def test_rev_three(execute_multiple_instructions):
    # rev 2 forward, stack is rotated to [4, 3, 2, 1], pop twice, return to nop
    assert execute_multiple_instructions(
        [ReverseInstruction, NopInstruction, PopInstruction],
        [1, 2, 3, 4, 2, 0],
        [
            ReverseInstruction.notation,
            PopInstruction.notation,
            PopInstruction.notation,
            NopInstruction.notation,
        ],
    ) == [3, 4]


def test_rev_four(execute_multiple_instructions):
    #  Leaves the program in reverse by jumping over the rev.
    assert execute_multiple_instructions(
        [ReverseInstruction, NopInstruction, GotoInstruction],
        [0, 1, 2, 3, 2, 0],
        [
            NopInstruction.notation,
            ReverseInstruction.notation,
            GotoInstruction.notation,
            NopInstruction.notation,
            NopInstruction.notation,
        ],
    ) == [3, 2, 1, 0]


def test_rev_five(execute_multiple_instructions):
    #  Leaves the program in reverse by jumping over the rev.
    assert execute_multiple_instructions(
        [ReverseInstruction, NopInstruction, GotoInstruction],
        [0, 1, 2, 3, 1, 0],
        [
            NopInstruction.notation,
            ReverseInstruction.notation,
            GotoInstruction.notation,
            NopInstruction.notation,
        ],
    ) == [3, 2, 1, 0]


def test_rev_nested_one(execute_multiple_instructions):
    #  Leaves the program in reverse by jumping over the rev.
    assert execute_multiple_instructions(
        [ReverseInstruction, NopInstruction, PopInstruction],
        [-1, 0, 2, -1, 10, 11, 12, -1, -1, 5, 0],
        [
            ReverseInstruction.notation,
            PopInstruction.notation,
            PopInstruction.notation,
            PopInstruction.notation,
            ReverseInstruction.notation,
            PopInstruction.notation,
            NopInstruction.notation,
        ],
    ) == [10, 11, 12]
