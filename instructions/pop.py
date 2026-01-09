
from .base_instruction import BaseInstruction


class PopInstruction(BaseInstruction):
    notation = "pop"

    @staticmethod
    def execute(stack: list[int]):
        stack.pop()
        return
