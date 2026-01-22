from .bulxor import BulxorInstruction


def test_bulxor(execute_single_instruction):
    assert execute_single_instruction(BulxorInstruction, [1, -1, 3, 3, 2]) == [1, 0]
