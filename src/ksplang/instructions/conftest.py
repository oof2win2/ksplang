from typing import Sequence

import pytest

from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


def execute_instruction(
    instruction_cls: type[BaseInstruction], stack: list[int]
) -> list[int]:
    ex = Executor([instruction_cls.notation], stack, [instruction_cls])
    ex.execute_program()
    return ex.get_stack()


def execute_multiple(
    available: Sequence[type[BaseInstruction]],
    stack: list[int],
    instructions: list[str],
) -> list[int]:
    ex = Executor(instructions, stack, available)
    ex.execute_program()
    return ex.get_stack()


@pytest.fixture
def execute_single_instruction():
    return execute_instruction


@pytest.fixture
def execute_multiple_instructions():
    return execute_multiple
