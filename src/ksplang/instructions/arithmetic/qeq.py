from math import sqrt

from ksplang.helpers.gcd import gcd
from ksplang.instructions.base_instruction import BaseInstruction


class QuadraticSolutionInstruction(BaseInstruction):
    notation = "qeq"

    @staticmethod
    def execute(stack: list[int]):
        a = stack.pop()
        b = stack.pop()
        c = stack.pop()

        sols = [
            (-b + sqrt(b**2 - 4 * a * c)) / (2 * a),
            (-b + sqrt(b**2 - 4 * a * c)) / (2 * a),
        ]
        sols.sort()
        for sol in sols:
            if sol.is_integer():
                stack.append(int(sol))

        return
