from math import fmod

from .base_instruction import BaseInstruction


class RemInstruction(BaseInstruction):
    notation = "REM"

    @staticmethod
    def execute(stack: list[int]):
        first = stack.pop()
        second = stack.pop()
        stack.append(int(fmod(first, second)))

        return
