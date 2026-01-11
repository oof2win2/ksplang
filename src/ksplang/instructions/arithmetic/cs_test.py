from .cs import CSInstruction


def test_cs(execute_single_instruction):
    assert execute_single_instruction(CSInstruction, [18]) == [18, 9]


def test_cs_negative(execute_single_instruction):
    assert execute_single_instruction(CSInstruction, [-18]) == [-18, 9]
