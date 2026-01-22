from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class MaxInstruction(BaseInstruction):
    notation = "max"

    @staticmethod
    def execute(executor: Executor):
        first = executor.stack_pop()
        second = executor.stack_pop()
        executor.stack_push(max(first, second))
        return
