from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class BrzInstruction(BaseInstruction):
    notation = "brz"

    @staticmethod
    def execute(executor: Executor):
        should = executor.stack_get(-1)
        address = executor.stack_get(-2)

        if should != 0:
            return

        # the Executor will auto-increment the IP after executing the instruction
        executor.set_instruction_pointer(address - 1)
        print(f"Setting IP to {address}")

        return
