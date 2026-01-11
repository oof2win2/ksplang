from ksplang.instructions.base_instruction import BaseInstruction


class LensumInstruction(BaseInstruction):
    notation = "lensum"

    @staticmethod
    def execute(stack: list[int]):
        first = stack.pop()
        second = stack.pop()
        lenfirst = len(str(abs(first))) if first != 0 else 0
        lensecond = len(str(abs(second))) if second != 0 else 0
        stack.append(lenfirst + lensecond)

        return
