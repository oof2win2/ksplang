from math import floor

from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction

from ...helpers.mergesort import mergesort


class MedianInstruction(BaseInstruction):
    notation = "m"

    @staticmethod
    def execute(executor: Executor):
        count = executor.stack_get(-1)
        numbers = [executor.stack_get(-2 - i) for i in range(count - 1)]
        numbers.append(count)

        # handle the count being one, no need to sort or anything
        if count == 1:
            executor.stack_push(numbers[0])
            return

        sorted = mergesort(numbers)
        mid = count // 2

        if count % 2 == 1:
            executor.stack_push(sorted[mid])
            return

        first = sorted[mid - 1]
        second = sorted[mid]
        executor.stack_push(floor((first + second) / 2))

        return
