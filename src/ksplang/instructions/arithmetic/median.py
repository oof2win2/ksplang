from math import floor

from ...helpers.mergesort import mergesort
from ksplang.instructions.base_instruction import BaseInstruction


class MedianInstruction(BaseInstruction):
    notation = "m"

    @staticmethod
    def execute(stack: list[int]):
        count = stack.pop()
        numbers = [stack.pop() for _ in range(count - 1)]
        numbers.append(count)

        # handle the count being one, no need to sort or anything
        if count == 1:
            stack.append(numbers[0])
            return

        sorted = mergesort(numbers)
        mid = count // 2

        if count % 2 == 1:
            stack.append(sorted[mid])
            return

        first = sorted[mid - 1]
        second = sorted[mid]
        stack.append(floor((first + second) / 2))

        return
