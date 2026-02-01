from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class GotoInstruction(BaseInstruction):
    notation = "goto"

    @staticmethod
    def execute(executor: Executor):
        ip = executor.stack_peek()

        if ip < 0:
            raise ValueError("Jump address must be non-negative")
        if ip > executor.get_program_size() - 1:
            raise ValueError("Jump address must be within program bounds")

        # the Executor will auto-increment the IP after executing the instruction
        executor.set_instruction_pointer(ip - 1 * executor.get_execution_direction())

        return
