from ksplang.helpers.int64 import is_int64
from ksplang.instructions.base_instruction import BaseInstruction


class SumInstruction(BaseInstruction):
    notation = "sum"

    @staticmethod
    def execute(stack: list[int]):
        total = 0
        while stack:
            total += stack.pop()
        if not is_int64(total):
            raise ValueError("[sum] instruction result is not a valid int64")

        stack.append(total)

        return
