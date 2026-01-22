from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction

from ...helpers.tetr import tetr


class TetrationInstruction(BaseInstruction):
    notation = "tetr"

    @staticmethod
    def execute(executor: Executor):
        number = executor.stack_pop()
        repetitions = executor.stack_pop()

        executor.stack_push(tetr(number, repetitions))

        return
