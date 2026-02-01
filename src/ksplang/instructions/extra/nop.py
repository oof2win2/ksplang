from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class NopInstruction(BaseInstruction):
    """
    No operation instruction.
    For testing purposes only.
    """

    notation = "nop"

    @staticmethod
    def execute(executor: Executor):
        return
