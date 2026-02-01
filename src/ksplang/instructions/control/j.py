from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class JumpInstruction(BaseInstruction):
    notation = "j"

    @staticmethod
    def execute(executor: Executor):
        address = executor.stack_peek()
        direction = executor.get_execution_direction()
        current = executor.get_instruction_pointer()

        if address < 0:
            raise ValueError("Jump address must be non-negative")
        if address > executor.get_program_size() - 1:
            raise ValueError("Jump address must be within program bounds")

        executor.set_instruction_pointer(current + address * direction)

        return
