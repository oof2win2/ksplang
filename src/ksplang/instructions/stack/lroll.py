from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class LRollInstruction(BaseInstruction):
    notation = "lroll"

    @staticmethod
    def execute(executor: Executor):
        n = executor.stack_pop()
        x = executor.stack_pop()

        # remove the last n items from the stack and the restore their order as in the stack
        nextn = [executor.stack_pop() for _ in range(n)]
        nextn.reverse()

        if x < 0:
            # x is negative, so we multiply by -1 for range to work as intended
            for _ in range(x * -1):
                nextn.append(nextn.pop(0))
        else:
            for _ in range(x):
                nextn.insert(0, nextn.pop())

        executor.stack_extend(nextn)
        return
