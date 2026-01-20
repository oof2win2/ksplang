from .bitand import AndInstruction


def test_and(execute_single_instruction):
    assert execute_single_instruction(AndInstruction, [5, 3]) == [1]
    assert execute_single_instruction(AndInstruction, [3, 3]) == [3]


def test_and_negative(execute_single_instruction):
    assert execute_single_instruction(AndInstruction, [-1, -1]) == [-1]
    assert execute_single_instruction(AndInstruction, [-1, 1]) == [1]
