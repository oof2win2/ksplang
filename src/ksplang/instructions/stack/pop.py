from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class PopInstruction(BaseInstruction):
    notation = "pop"

    @staticmethod
    def execute(executor: Executor):
        executor.stack_pop()
        return
