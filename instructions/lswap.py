from .base_instruction import BaseInstruction


class LSwapInstruction(BaseInstruction):
    notation = "l-swap"

    @staticmethod
    def execute(stack: list[int]):
        if len(stack) == 0:
            raise IndexError("Stack is empty")
        # swap the values
        tmp = stack[0]
        stack[0] = stack[-1]
        stack[-1] = tmp
        return
