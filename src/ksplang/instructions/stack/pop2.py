from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class Pop2Instruction(BaseInstruction):
    notation = "pop2"

    @staticmethod
    def execute(executor: Executor):
        executor.stack_pop(-2)
        return
