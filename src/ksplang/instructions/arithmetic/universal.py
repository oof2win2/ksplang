import math

from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class UniversalMathInstruction(BaseInstruction):
    notation = "u"

    @staticmethod
    def execute(executor: Executor):
        id = executor.stack_pop()

        if id == 0:
            executor.stack_push(executor.stack_pop() + executor.stack_pop())
            return

        if id == 1:
            first = executor.stack_pop()
            second = executor.stack_pop()
            executor.stack_push(abs(first - second))
            return

        if id == 2:
            executor.stack_push(executor.stack_pop() * executor.stack_pop())
            return

        if id == 3:
            first = executor.stack_pop()
            second = executor.stack_pop()
            # must behave like C modulo
            rem = int(math.fmod(first, second))

            if rem == 0:
                executor.stack_push(int(first / second))
            else:
                executor.stack_push(rem)
            return

        if id == 4:
            executor.stack_push(math.factorial(executor.stack_pop()))
            return

        if id == 5:
            next = executor.stack_pop()
            if next < 0:
                executor.stack_push(-1)
            elif next == 0:
                executor.stack_push(0)
            else:
                executor.stack_push(1)
            return

        raise ValueError(f"[u]: Unsupported operand ID {id}")
