from ..constants import MAX_STACK_SIZE, MIN_INT
from .base_instruction import BaseInstruction


class FFInstruction(BaseInstruction):
    notation = "-ff"

    @staticmethod
    def execute(stack: list[int]):
        first = stack.pop()
        second = stack.pop()

        print(first, second)
        if first == 2 and second == 4:
            return

        # replace stack with -2^63
        stack.clear()
        stack.extend([MIN_INT] * MAX_STACK_SIZE)

        return
