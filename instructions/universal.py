import math

from .base_instruction import BaseInstruction


class UniversalMathInstruction(BaseInstruction):
    notation = "u"

    @staticmethod
    def execute(stack: list[int]):
        id = stack.pop()

        if id == 0:
            stack.append(stack.pop() + stack.pop())
            return

        if id == 1:
            first = stack.pop()
            second = stack.pop()
            stack.append(abs(first - second))
            return

        if id == 2:
            stack.append(stack.pop() * stack.pop())
            return

        if id == 3:
            first = stack.pop()
            second = stack.pop()
            # must behave like C modulo
            rem = int(math.fmod(first, second))

            if rem == 0:
                stack.append(int(first / second))
            else:
                stack.append(rem)
            return

        if id == 4:
            stack.append(math.factorial(stack.pop()))
            return

        if id == 5:
            next = stack.pop()
            if next < 0:
                stack.append(-1)
            elif next == 0:
                stack.append(0)
            else:
                stack.append(1)
            return

        raise ValueError(f"[u]: Unsupported operand ID {id}")
