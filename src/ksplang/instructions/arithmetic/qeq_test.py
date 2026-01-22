from .qeq import QuadraticSolutionInstruction


def test_qeq_two_integer_solutions(execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [6, -5, 1]) == [
        3,
        3,
    ]


def test_qeq_one_integer_solution(execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [1, -2, 1]) == [
        1,
        1,
    ]


def test_qeq_negative_coefficients(execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [9, 0, -1]) == [
        -3,
        -3,
    ]


def test_qeq_large_coefficients(execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [16, -10, 1]) == [
        8,
        8,
    ]


def test_qeq_no_real_solutions(execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [-1, 0, 1]) == [
        1,
        1,
    ]


def test_qeq_duplicate_solutions(execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [9, -6, 1]) == [
        3,
        3,
    ]


def test_qeq_negative_solution(execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [12, 13, 1]) == [
        -1,
        -1,
    ]


def test_qeq_simple(execute_single_instruction):
    assert execute_single_instruction(QuadraticSolutionInstruction, [-4, 0, 1]) == [
        2,
        2,
    ]
