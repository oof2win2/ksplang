from ksplang.executor import Executor
from ksplang.helpers.int64 import to_int64
from ksplang.instructions.base_instruction import BaseInstruction


# the range of numbers is 2^63-1 to -2^63, and the first bit is the sign bit
# since python has no comprehension of twos complement, we need to implement it ourselves
def bitshift(num: int, numshifts: int):
    # if the number is positive, we can just shift left naturally
    res = num << numshifts
    # mask to 64 bits, simulates the arithmetic overflow (doesn't exist in python)
    # res = res & ((1 << 64) - 1)

    # # if the 63rd bit is set, we need to subtract 2^64 to simulate the overflow
    # if res & (1 << 63):
    #     res = res - (1 << 64)

    return to_int64(res)


class BitshiftInstruction(BaseInstruction):
    id = 18
    notation = "bitshift"

    @staticmethod
    def execute(executor: Executor):
        numshifts = executor.stack_pop()
        if numshifts < 0:
            raise ValueError("[bitshift] Number of bits to shift must be non-negative")
        num = executor.stack_pop()
        result = bitshift(num, numshifts)
        executor.stack_push(result)

        return
