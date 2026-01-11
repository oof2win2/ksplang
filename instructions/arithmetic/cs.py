from ..base_instruction import BaseInstruction


class CSInstruction(BaseInstruction):
    notation = "CS"

    @staticmethod
    def execute(stack: list[int]):
        num = str(abs(stack[-1]))
        sum = 0
        for char in num:
            sum += int(char)
        stack.append(sum)

        return
