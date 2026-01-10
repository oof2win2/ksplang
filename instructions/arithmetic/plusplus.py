from ..base_instruction import BaseInstruction


class PlusPlusInstruction(BaseInstruction):
    notation = "++"

    @staticmethod
    def execute(stack: list[int]):
        if len(stack) == 0:
            raise ValueError("Stack is empty")
        stack.append(stack.pop() + 1)
        return
