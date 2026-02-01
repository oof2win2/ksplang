from ksplang.executor import Executor
from ksplang.helpers.int64 import is_int64
from ksplang.instructions.base_instruction import BaseInstruction


class SumInstruction(BaseInstruction):
    id = 20
    notation = "sum"

    @staticmethod
    def execute(executor: Executor):
        total = 0
        while executor.stack_len() > 0:
            total += executor.stack_pop()
        if not is_int64(total):
            raise ValueError("[sum] instruction result is not a valid int64")

        executor.stack_push(total)

        return
