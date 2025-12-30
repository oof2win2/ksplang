from logging import debug
from typing import Sequence

from .instructions.base_instruction import BaseInstruction


def execute_program(
    init_instructions: list,
    init_stack: list[int],
    # sequence means all available instructions must extend from BaseInstruction
    available_instructions: Sequence[type[BaseInstruction]],
):
    instructions = init_instructions[::]
    stack = init_stack[::]
    for i, instruction in enumerate(instructions):
        ex = next(
            (ins for ins in available_instructions if ins.notation == instruction), None
        )
        if not ex:
            raise ValueError(f"Unknown instruction: {instruction}")
        ex.execute(stack)
        debug(f"Executed instruction {instruction} on stack {stack}")

    return stack
