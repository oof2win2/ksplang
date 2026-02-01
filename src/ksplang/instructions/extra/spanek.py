from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class SpanekInstruction(BaseInstruction):
    id = 31
    notation = "spanek"

    @staticmethod
    def execute(executor: Executor):
        raise TimeoutError("Timed out")
