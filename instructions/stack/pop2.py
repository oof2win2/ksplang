from ..base_instruction import BaseInstruction


class Pop2Instruction(BaseInstruction):
    notation = "pop2"

    @staticmethod
    def execute(stack: list[int]):
        stack.pop(-2)
        return
