from ksplang.helpers.gcd import gcd
from ksplang.instructions.base_instruction import BaseInstruction


class GCDManyInstruction(BaseInstruction):
    notation = "d"

    @staticmethod
    def execute(stack: list[int]):
        count = stack.pop()
        numbers = [stack.pop() for _ in range(count)]

        stack.append(gcd(*numbers))

        return
