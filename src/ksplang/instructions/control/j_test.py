import pytest

from ksplang.executor import Executor
from ksplang.instructions.arithmetic.plusplus import PlusPlusInstruction

from .j import JumpInstruction


def test_jump_skip_one(execute_multiple_instructions):
    # assert it skips one plusplus
    assert execute_multiple_instructions(
        [JumpInstruction, PlusPlusInstruction],
        [1],
        [
            JumpInstruction.notation,
            PlusPlusInstruction.notation,
            PlusPlusInstruction.notation,
        ],
    ) == [2]


def test_jump_skip_two(execute_multiple_instructions):
    # assert it skips two plusplus
    assert execute_multiple_instructions(
        [JumpInstruction, PlusPlusInstruction],
        [2],
        [
            JumpInstruction.notation,
            PlusPlusInstruction.notation,
            PlusPlusInstruction.notation,
        ],
    ) == [2]


def test_jump_oob_below(execute_multiple_instructions):
    with pytest.raises(ValueError):
        execute_multiple_instructions(
            [JumpInstruction],
            [-5],
            [
                JumpInstruction.notation,
            ],
        )


def test_jump_oob_above(execute_multiple_instructions):
    with pytest.raises(ValueError):
        execute_multiple_instructions(
            [JumpInstruction],
            [2],
            [
                JumpInstruction.notation,
            ],
        )
