from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class BrzInstruction(BaseInstruction):
    id = 26
    notation = "brz"

    @staticmethod
    def execute(executor: Executor):
        should = executor.stack_get(-1)
        address = executor.stack_get(-2)

        if address < 0:
            raise ValueError("Jump address must be non-negative")
        if address > executor.get_program_size() - 1:
            raise ValueError("Jump address must be within program bounds")

        if should != 0:
            return

        # the Executor will auto-increment the IP after executing the instruction
        executor.set_instruction_pointer(address - 1)

        return
