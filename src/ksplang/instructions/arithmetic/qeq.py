from math import sqrt

from ksplang.executor import Executor
from ksplang.helpers.solve_quadratic_equation import solve_qeq
from ksplang.instructions.base_instruction import BaseInstruction


class QuadraticSolutionInstruction(BaseInstruction):
    id = 23
    notation = "qeq"

    @staticmethod
    def execute(executor: Executor):
        a = executor.stack_pop()
        b = executor.stack_pop()
        c = executor.stack_pop()

        sols = solve_qeq(a, b, c)

        for sol in sols:
            executor.stack_push(int(sol))
        return
