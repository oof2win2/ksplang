from .lensum import LensumInstruction


def test_lensum_one(execute_single_instruction):
    assert execute_single_instruction(LensumInstruction, [0, 0]) == [0]


def test_lensum_two(execute_single_instruction):
    assert execute_single_instruction(LensumInstruction, [3, 2]) == [2]


def test_lensum_three(execute_single_instruction):
    assert execute_single_instruction(LensumInstruction, [-3, 2]) == [2]


def test_lensum_four(execute_single_instruction):
    assert execute_single_instruction(LensumInstruction, [-22, 22]) == [4]
