import pytest
from _pytest.runner import CallInfo

from ksplang.executor import Executor
from ksplang.instructions.arithmetic.plusplus import PlusPlusInstruction
from ksplang.instructions.extra.nop import NopInstruction

from .call import CallInstruction


def test_call_one(execute_multiple_instructions):
    instructions = [
        CallInstruction.notation,
        NopInstruction.notation,
        NopInstruction.notation,
        NopInstruction.notation,
        NopInstruction.notation,
    ]
    assert execute_multiple_instructions(
        [NopInstruction, CallInstruction], [1, 2, 3, 4], instructions
    ) == [1, 2, 3, 4, 1]


def test_call_two(execute_multiple_instructions):
    instructions = [
        NopInstruction.notation,
        CallInstruction.notation,
        NopInstruction.notation,
        NopInstruction.notation,
        NopInstruction.notation,
    ]
    assert execute_multiple_instructions(
        [NopInstruction, CallInstruction], [1, 2, 3], instructions
    ) == [1, 2, 3, 2]


def test_call_three(execute_multiple_instructions):
    instructions = [
        NopInstruction.notation,
        NopInstruction.notation,
        NopInstruction.notation,
        NopInstruction.notation,
        CallInstruction.notation,
        NopInstruction.notation,
    ]
    assert execute_multiple_instructions(
        [NopInstruction, CallInstruction], [1, 2, 3], instructions
    ) == [1, 2, 3, 5, 5]


def test_call_low(execute_multiple_instructions):
    ex = Executor(
        [
            CallInstruction.notation,
        ],
        [-1],
        [CallInstruction],
    )
    with pytest.raises(ValueError):
        ex.execute_program()


def test_call_high(execute_multiple_instructions):
    ex = Executor(
        [
            CallInstruction.notation,
        ],
        [1],
        [CallInstruction],
    )
    with pytest.raises(ValueError):
        ex.execute_program()
