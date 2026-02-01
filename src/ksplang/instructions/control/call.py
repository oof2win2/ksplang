from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class CallInstruction(BaseInstruction):
    id = 27
    notation = "call"

    @staticmethod
    def execute(executor: Executor):
        ip = executor.stack_peek()

        current_ip = executor.get_instruction_pointer()

        if ip < 0:
            raise ValueError("Jump address must be non-negative")
        if ip > executor.get_program_size() - 1:
            raise ValueError("Jump address must be within program bounds")
        if executor.get_execution_direction() == 1:
            executor.stack_push(current_ip + 1)
        else:
            executor.stack_push(current_ip - 1)

        # the Executor will auto-increment the IP after executing the instruction
        executor.set_instruction_pointer(ip - 1)

        return
