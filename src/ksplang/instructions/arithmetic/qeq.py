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

        sols = [
            (-b + sqrt(b**2 - 4 * a * c)) / (2 * a),
            (-b + sqrt(b**2 - 4 * a * c)) / (2 * a),
        ]
        sols.sort()
        for sol in sols:
            if sol.is_integer():
                executor.stack_push(int(sol))

        return
