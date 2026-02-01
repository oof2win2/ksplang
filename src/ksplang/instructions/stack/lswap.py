from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class LSwapInstruction(BaseInstruction):
    id = 4
    notation = "l-swap"

    @staticmethod
    def execute(executor: Executor):
        if executor.stack_len() == 0:
            raise IndexError("Stack is empty")
        # swap the values
        tmp = executor.stack_get(0)
        executor.stack_set(0, executor.stack_get(-1))
        executor.stack_set(-1, tmp)
        return
