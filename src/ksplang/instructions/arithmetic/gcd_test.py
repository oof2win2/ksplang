from .gcd import GCDInstruction


def test_gcd_zero(execute_single_instruction):
    assert execute_single_instruction(GCDInstruction, [9, 0, 5]) == [9, 5]


def test_gcd_one(execute_single_instruction):
    assert execute_single_instruction(GCDInstruction, [9, 1, 5]) == [9, 1]


def test_gcd_three(execute_single_instruction):
    assert execute_single_instruction(GCDInstruction, [9, 6, 15]) == [9, 3]


def test_gcd_negative(execute_single_instruction):
    assert execute_single_instruction(GCDInstruction, [-6, 15]) == [3]
