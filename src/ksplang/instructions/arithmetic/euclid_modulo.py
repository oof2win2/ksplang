from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class EuclidianModuloInstruction(BaseInstruction):
    id = 12
    notation = "%"

    @staticmethod
    def execute(executor: Executor):
        first = executor.stack_pop()
        second = executor.stack_pop()
        executor.stack_push(first % abs(second))

        return
