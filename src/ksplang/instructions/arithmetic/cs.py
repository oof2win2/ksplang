from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class CSInstruction(BaseInstruction):
    id = 16
    notation = "CS"

    @staticmethod
    def execute(executor: Executor):
        num = str(abs(executor.stack_get(-1)))
        sum = 0
        for char in num:
            sum += int(char)
        executor.stack_push(sum)

        return
