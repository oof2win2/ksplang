from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction

from ...constants import MAX_STACK_SIZE, MIN_INT


class FFInstruction(BaseInstruction):
    notation = "-ff"

    @staticmethod
    def execute(executor: Executor):
        first = executor.stack_pop()
        second = executor.stack_pop()

        print(first, second)
        if first == 2 and second == 4:
            return

        # replace stack with -2^63
        executor.stack_clear()
        executor.stack_extend([MIN_INT] * MAX_STACK_SIZE)

        return
