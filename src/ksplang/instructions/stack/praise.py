from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class PraiseInstruction(BaseInstruction):
    id = 0
    notation = "praise"

    @staticmethod
    def execute(executor: Executor):
        times = executor.stack_pop()
        if times < 0:
            raise ValueError("Praise times must be non-negative")
        for _ in range(times):
            executor.stack_extend([77, 225, 109, 32, 114, 225, 100, 32, 75, 83, 80])
        return
