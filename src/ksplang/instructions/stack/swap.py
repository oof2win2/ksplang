from ksplang.instructions.base_instruction import BaseInstruction


class SwapInstruction(BaseInstruction):
    notation = "swap"

    @staticmethod
    def execute(stack: list[int]):
        index = stack.pop()
        toswap = stack.pop()

        if index < 0:
            raise IndexError("[swap]: Index to swap with cannot be negative")
        if index > len(stack):
            raise IndexError("[swap]: Index to swap with out of bounds")

        tmp = stack[index]
        stack[index] = toswap
        stack.append(tmp)

        return
