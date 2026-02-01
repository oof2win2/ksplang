import pytest

from ksplang.executor import Executor
from ksplang.instructions.arithmetic.plusplus import PlusPlusInstruction

from .goto import GotoInstruction


def test_goto_set_ip(execute_multiple_instructions):
    ex = Executor(
        [
            GotoInstruction.id,
            PlusPlusInstruction.id,
            PlusPlusInstruction.id,
        ],
        [2, 2],
        [GotoInstruction, PlusPlusInstruction],
    )
    ex.execute_program()
    # the stack should have only one PlusPlus executed on it
    # 2 should be popped (IP) and increment the other 2 => 3
    assert ex.get_stack() == [2, 3]
    # the IP should be set to 3, the last ++ instruction
    assert ex.get_instruction_pointer() == 3
    # the number of executed instructions should be 2
    # one BRZ and one ++
    assert ex.get_executed_instructions_count() == 2


def test_goto_low(execute_multiple_instructions):
    ex = Executor(
        [
            GotoInstruction.id,
        ],
        [-1],
        [GotoInstruction],
    )
    with pytest.raises(ValueError):
        ex.execute_program()


def test_goto_high(execute_multiple_instructions):
    ex = Executor(
        [
            GotoInstruction.id,
        ],
        [1],
        [GotoInstruction],
    )
    with pytest.raises(ValueError):
        ex.execute_program()
