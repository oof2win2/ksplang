from .base_instruction import BaseInstruction


class PraiseInstruction(BaseInstruction):
    notation = "praise"

    @staticmethod
    def execute(stack: list[int]):
        times = stack.pop()
        if times < 0:
            raise ValueError("Praise times must be non-negative")
        for _ in range(times):
            stack.extend([77, 225, 109, 32, 114, 225, 100, 32, 75, 83, 80])
        return
