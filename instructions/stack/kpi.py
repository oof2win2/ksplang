from math import pi

from ..base_instruction import BaseInstruction

pidigits = "31415926535897932384626433832795028841971693993751"


class KPIInstruction(BaseInstruction):
    notation = "kPi"

    @staticmethod
    def execute(stack: list[int]):
        found = False
        for i in range(len(stack) - 1, -1, -1):
            if i == stack[i]:
                stack[i] = int(pidigits[i])
                found = True
                break

        # if it doesn't find any match, replace the whole stack with digits of pi
        if not found:
            for i in range(len(stack)):
                stack[i] = int(pidigits[i])

        return
