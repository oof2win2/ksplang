from ksplang.helpers.int64 import to_int64
from ksplang.instructions.base_instruction import BaseInstruction


class AndInstruction(BaseInstruction):
    notation = "And"

    @staticmethod
    def execute(stack: list[int]):
        first = stack.pop()
        second = stack.pop()

        # we do a bitwise AND. numbers are represented as C int64 with two's complement
        res = first & second

        stack.append(to_int64(res))

        return
