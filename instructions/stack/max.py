from ..base_instruction import BaseInstruction


class MaxInstruction(BaseInstruction):
    notation = "max"

    @staticmethod
    def execute(stack: list[int]):
        first = stack.pop()
        second = stack.pop()
        stack.append(max(first, second))
        return
