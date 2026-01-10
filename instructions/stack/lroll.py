from ..base_instruction import BaseInstruction


class LRollInstruction(BaseInstruction):
    notation = "lroll"

    @staticmethod
    def execute(stack: list[int]):
        n = stack.pop()
        x = stack.pop()

        # remove the last n items from the stack and the restore their order as in the stack
        nextn = [stack.pop() for _ in range(n)]
        nextn.reverse()

        if x < 0:
            # x is negative, so we multiply by -1 for range to work as intended
            for _ in range(x * -1):
                nextn.append(nextn.pop(0))
                print(nextn)
        else:
            for _ in range(x):
                nextn.insert(0, nextn.pop())

        stack.extend(nextn)
        return
