from ksplang.helpers.gcd import gcd
from ksplang.instructions.base_instruction import BaseInstruction


class GCDInstruction(BaseInstruction):
    notation = "gcd"

    @staticmethod
    def execute(stack: list[int]):
        first = stack.pop()
        second = stack.pop()

        stack.append(gcd(first, second))

        return
