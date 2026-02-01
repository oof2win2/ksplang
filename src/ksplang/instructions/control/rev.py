from ksplang.executor import Executor
from ksplang.helpers.solve_quadratic_equation import solve_qeq
from ksplang.instructions.base_instruction import BaseInstruction


class ReverseInstruction(BaseInstruction):
    id = 30
    notation = "rev"

    @staticmethod
    def execute(executor: Executor):
        a = executor.stack_pop()
        b = executor.stack_pop()

        if a < 0 or b < 0:
            raise ValueError("[rev]: Addresses must be non-negative")

        offset = None
        if a == 0:
            offset = b
        else:
            c = executor.stack_pop()
            if c < 0:
                raise ValueError("[rev]: Offset must be non-negative")
            sols = solve_qeq(a, b, c)
            if len(sols) == 0:
                offset = b
            elif len(sols) == 1:
                offset = sols[0]
            else:
                offset = max(sols[0], sols[1])

        current_ip = executor.get_instruction_pointer()
        # subtract if reversed
        return_ip = current_ip + (offset + 1) * executor.get_execution_direction()
        new_ip = current_ip + (offset + 1) * executor.get_execution_direction()

        if return_ip < 0:
            raise ValueError("[rev]: Return IP must be non-negative")
        if return_ip > executor.get_program_size():
            raise ValueError("[rev]: Return IP must be within the program")

        executor.append_rev_stack((current_ip, return_ip))

        executor.set_instruction_pointer(new_ip)
        executor.set_execution_direction(executor.get_execution_direction() * -1)

        executor.stack_reverse()

        return
