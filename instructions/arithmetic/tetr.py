from ...helpers.tetr import tetr
from ..base_instruction import BaseInstruction


class TetrationInstruction(BaseInstruction):
    notation = "tetr"

    @staticmethod
    def execute(stack: list[int]):
        number = stack.pop()
        repetitions = stack.pop()

        stack.append(tetr(number, repetitions))

        return
