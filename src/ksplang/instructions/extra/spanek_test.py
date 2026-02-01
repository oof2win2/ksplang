import pytest

from ksplang.instructions.extra.spanek import SpanekInstruction


def test_spanek_instruction_empty(execute_single_instruction):
    with pytest.raises(TimeoutError):
        execute_single_instruction(SpanekInstruction, [])


def test_spanek_instruction_nonempty(execute_single_instruction):
    with pytest.raises(TimeoutError):
        execute_single_instruction(SpanekInstruction, [1, 2, 3])
