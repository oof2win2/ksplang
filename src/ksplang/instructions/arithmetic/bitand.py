from ksplang.executor import Executor
from ksplang.helpers.int64 import to_int64
from ksplang.instructions.base_instruction import BaseInstruction


class AndInstruction(BaseInstruction):
    id = 19
    notation = "And"

    @staticmethod
    def execute(executor: Executor):
        first = executor.stack_pop()
        second = executor.stack_pop()

        # we do a bitwise AND. numbers are represented as C int64 with two's complement
        res = first & second

        executor.stack_push(to_int64(res))

        return
