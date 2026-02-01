from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class PlusPlusInstruction(BaseInstruction):
    id = 9
    notation = "++"

    @staticmethod
    def execute(executor: Executor):
        if executor.stack_len() == 0:
            raise ValueError("Stack is empty")
        executor.stack_push(executor.stack_pop() + 1)
        return
