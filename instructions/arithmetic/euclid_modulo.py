from ..base_instruction import BaseInstruction


class EuclidianModuloInstruction(BaseInstruction):
    notation = "%"

    @staticmethod
    def execute(stack: list[int]):
        first = stack.pop()
        second = stack.pop()
        stack.append(first % abs(second))

        return
