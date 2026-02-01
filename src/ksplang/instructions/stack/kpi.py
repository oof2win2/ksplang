from math import pi

from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction

pidigits = "31415926535897932384626433832795028841971693993751"


class KPIInstruction(BaseInstruction):
    id = 8
    notation = "kPi"

    @staticmethod
    def execute(executor: Executor):
        found = False
        for i in range(executor.stack_len() - 1, -1, -1):
            if i == executor.stack_get(i):
                executor.stack_set(i, int(pidigits[i]))
                found = True
                break

        # if it doesn't find any match, replace the whole stack with digits of pi
        if not found:
            for i in range(executor.stack_len()):
                executor.stack_set(i, int(pidigits[i]))

        return
