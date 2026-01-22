from math import sqrt

from ksplang.executor import Executor
from ksplang.helpers.gcd import gcd
from ksplang.instructions.base_instruction import BaseInstruction


class QuadraticSolutionInstruction(BaseInstruction):
    notation = "qeq"

    @staticmethod
    def execute(executor: Executor):
        a = executor.stack_pop()
        b = executor.stack_pop()
        c = executor.stack_pop()

        if a == 0 and b == 0:
            # c == 0 equation, infinite solutions
            if c == 0:
                raise ValueError("[qeq] The equation is indeterminate.")
            # for c != 0, there are no solutions
            return

        if a == 0:
            # linear equation
            sol = -c / b
            if sol.is_integer():
                executor.stack_push(int(sol))
            return

        sols = [
            (-b + sqrt(b**2 - 4 * a * c)) / (2 * a),
            (-b - sqrt(b**2 - 4 * a * c)) / (2 * a),
        ]
        sols.sort()
        # if only one root, remove the duplicate
        if sols[0] == sols[1]:
            sols = [sols[0]]
        for sol in sols:
            if sol.is_integer():
                executor.stack_push(int(sol))
        return
