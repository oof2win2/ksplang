import pytest

from ksplang.executor import Executor
from ksplang.instructions.arithmetic.plusplus import PlusPlusInstruction

from .call import CallInstruction


def test_brz_set_ip(execute_multiple_instructions):
    ex = Executor(
        [
            CallInstruction.notation,
            PlusPlusInstruction.notation,
            PlusPlusInstruction.notation,
        ],
        [2, 2],
        [CallInstruction, PlusPlusInstruction],
    )
    ex.execute_program()
    # the stack should have only one PlusPlus executed on it
    # 2 should stay, but it should append IP+1 and increment that => 4
    assert ex.get_stack() == [2, 4]
    # the IP should be set to 3, the last ++ instruction
    assert ex.get_instruction_pointer() == 3
    # the number of executed instructions should be 2
    # one BRZ and one ++
    assert ex.get_executed_instructions_count() == 2


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
