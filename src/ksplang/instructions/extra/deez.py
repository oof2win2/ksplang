from ksplang.execute import discover_instructions, operator_by_id
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

        # instructions = []
        # for id in instruction_ids:
        #     if id < 0:
        #         raise ValueError("[deez]: Instruction ID must be non-negative")
        #     instructions.append(operator_by_id(id))

        print(instruction_ids)
        subprogram = Executor(instruction_ids, [], discover_instructions())
        subprogram.execute_program()
        stack = subprogram.get_stack()
        # print(stack, "subprogram stack")
        # executor.stack_extend(stack)
        for instruction_id in stack:
            executor.add_instruction(instruction_id)

        return
