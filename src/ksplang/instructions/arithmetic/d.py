from ksplang.executor import Executor
from ksplang.helpers.gcd import gcd
from ksplang.instructions.base_instruction import BaseInstruction


class GCDManyInstruction(BaseInstruction):
    notation = "d"

    @staticmethod
    def execute(executor: Executor):
        count = executor.stack_pop()
        numbers = [executor.stack_pop() for _ in range(count)]

        executor.stack_push(gcd(*numbers))

        return
