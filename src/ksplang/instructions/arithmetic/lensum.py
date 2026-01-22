from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class LensumInstruction(BaseInstruction):
    notation = "lensum"

    @staticmethod
    def execute(executor: Executor):
        first = executor.stack_pop()
        second = executor.stack_pop()
        lenfirst = len(str(abs(first))) if first != 0 else 0
        lensecond = len(str(abs(second))) if second != 0 else 0
        executor.stack_push(lenfirst + lensecond)

        return
