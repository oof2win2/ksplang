import pytest

from .qeq import QuadraticSolutionInstruction


@pytest.mark.parametrize(
    "a,b,c,sols",
    [
        # (x + 5)(x - 8)
        # x^2 - 3x - 40 = 0
        (-40, -3, 1, [-5, 8]),
        # (x - 3)(x - 3) -> only one root, 3
        (9, -6, 1, [3]),
        # no real solutions
        (-7, 3, 1, []),
    ],
)
def test_qeq_quadratic(a, b, c, sols, execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [a, b, c]) == sols


@pytest.mark.parametrize(
    "a,b,c,sols",
    [
        # 2x+4 = 0 -> x = -2
        (4, 2, 0, [-2]),
        # 2x + 3 = 0 -> x not an int
        (3, 2, 0, []),
        # 4x = 0 -> no sols
        (4, 0, 0, []),
    ],
)
def test_qeq_linear(a, b, c, sols, execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [a, b, c]) == sols
