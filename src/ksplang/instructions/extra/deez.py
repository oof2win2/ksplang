from ksplang.executor import Executor
from ksplang.helpers.solve_quadratic_equation import solve_qeq
from ksplang.instructions.base_instruction import BaseInstruction


class DeezInstruction(BaseInstruction):
    id = 32
    notation = "deez"

    @staticmethod
    def execute(executor: Executor):
        count = executor.stack_pop()
        if count < 0:
            raise ValueError("[deez]: Count must be non-negative")

        if executor.stack_len() < count:
            raise ValueError("[deez]: Not enough elements on stack")

        instruction_ids = [executor.stack_pop() for _ in range(count)]

        return
