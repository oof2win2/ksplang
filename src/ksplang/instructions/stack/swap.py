from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class SwapInstruction(BaseInstruction):
    notation = "swap"

    @staticmethod
    def execute(executor: Executor):
        index = executor.stack_pop()
        toswap = executor.stack_pop()

        if index < 0:
            raise IndexError("[swap]: Index to swap with cannot be negative")
        if index > executor.stack_len():
            raise IndexError("[swap]: Index to swap with out of bounds")

        tmp = executor.stack_get(index)
        executor.stack_set(index, toswap)
        executor.stack_push(tmp)

        return
