from ksplang.executor import Executor
from ksplang.helpers.solve_quadratic_equation import solve_qeq
from ksplang.instructions.base_instruction import BaseInstruction


class ReverseInstruction(BaseInstruction):
    notation = "rev"

    @staticmethod
    def execute(executor: Executor):
        revstack = executor.peek_rev_stack()
        if revstack and revstack["origin_ip"] == executor.get_instruction_pointer():
            executor.pop_rev_stack()  # close the block
            # reverse stack
            executor.stack_reverse()
            # reverse the execution direction
            executor.set_execution_direction(executor.get_execution_direction() * -1)
            # set the IP to the return IP
            executor.set_instruction_pointer(revstack["return_ip"] - 1)
            return

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
        target_ip = current_ip + offset
        return_ip = current_ip + offset + 1

        executor.set_instruction_pointer(target_ip + 1)
        executor.set_execution_direction(-1)
        executor.append_rev_stack({"origin_ip": current_ip, "return_ip": return_ip})

        executor.stack_reverse()

        return
