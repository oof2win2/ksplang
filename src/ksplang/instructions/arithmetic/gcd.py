from ksplang.executor import Executor
from ksplang.helpers.gcd import gcd
from ksplang.instructions.base_instruction import BaseInstruction


class GCDInstruction(BaseInstruction):
    notation = "gcd"

    @staticmethod
    def execute(executor: Executor):
        first = executor.stack_pop()
        second = executor.stack_pop()

        executor.stack_push(gcd(first, second))

        return
