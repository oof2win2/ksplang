from math import fmod

from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class RemInstruction(BaseInstruction):
    notation = "REM"

    @staticmethod
    def execute(executor: Executor):
        first = executor.stack_pop()
        second = executor.stack_pop()
        executor.stack_push(int(fmod(first, second)))

        return
