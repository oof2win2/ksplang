from ksplang.executor import Executor
from ksplang.instructions.base_instruction import BaseInstruction


class BulxorInstruction(BaseInstruction):
    notation = "bulxor"

    @staticmethod
    def execute(executor: Executor):
        count = executor.stack_pop()
        numbers = [executor.stack_pop() for _ in range(count * 2)]
        toadd = []
        for i in range(0, len(numbers), 2):
            first = 1 if numbers[i] > 0 else 0
            second = 1 if numbers[i + 1] > 0 else 0
            print(first, second, first ^ second)
            toadd.append(first ^ second)
        toadd.reverse()
        executor.stack_extend(toadd)

        return
