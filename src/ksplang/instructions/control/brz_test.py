import pytest

from ksplang.executor import Executor
from ksplang.instructions.arithmetic.plusplus import PlusPlusInstruction

from .brz import BrzInstruction


def test_brz_set_ip(execute_multiple_instructions):
    ex = Executor(
        [
            BrzInstruction.notation,
            PlusPlusInstruction.notation,
            PlusPlusInstruction.notation,
        ],
        [2, 0],
        [BrzInstruction, PlusPlusInstruction],
    )
    ex.execute_program()
    # the stack should have only one PlusPlus executed on it
    assert ex.get_stack() == [2, 1]
    # the IP should be set to 3, the last ++ instruction
    assert ex.get_instruction_pointer() == 3
    # the number of executed instructions should be 2
    # one BRZ and one ++
    assert ex.get_executed_instructions_count() == 2


def test_brz_ignore(execute_multiple_instructions):
    ex = Executor(
        [
            BrzInstruction.notation,
        ],
        [0, 1],
        [BrzInstruction],
    )
    # initial should be zero
    assert ex.get_instruction_pointer() == 0
    ex.execute_program()
    # BRZ should do nothing in this case, just increment IP by 1
    assert ex.get_instruction_pointer() == 1


def test_brz_infinite_loop(execute_multiple_instructions):
    ex = Executor(
        [
            BrzInstruction.notation,
            PlusPlusInstruction.notation,
            PlusPlusInstruction.notation,
        ],
        [0, 0],
        [BrzInstruction, PlusPlusInstruction],
    )
    assert ex.get_instruction_pointer() == 0
    # execute one step of the program, just the BrzInstruction
    numsteps = 4
    for _ in range(numsteps):
        ex.step()
    # BRZ should keep jumping back to the beginning
    assert ex.get_instruction_pointer() == 0
    # the number of executed instructions should be 4
    assert ex.get_executed_instructions_count() == numsteps


def test_brz_low(execute_multiple_instructions):
    ex = Executor(
        [
            BrzInstruction.notation,
        ],
        [-1, 0],
        [BrzInstruction],
    )
    with pytest.raises(ValueError):
        ex.execute_program()


def test_brz_high(execute_multiple_instructions):
    ex = Executor(
        [
            BrzInstruction.notation,
        ],
        [1, 0],
        [BrzInstruction],
    )
    with pytest.raises(ValueError):
        ex.execute_program()
