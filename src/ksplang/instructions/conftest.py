import pytest

from ksplang.execute import execute_program
from ksplang.instructions.base_instruction import BaseInstruction


def execute_instruction(
    instruction_cls: type[BaseInstruction], stack: list[int]
) -> list[int]:
    return execute_program([instruction_cls.notation], stack, [instruction_cls])


@pytest.fixture
def execute_single_instruction():
    return execute_instruction
