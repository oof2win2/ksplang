from .funkcia import FunkciaInstruction


def test_funkcia_source(execute_single_instruction):
    assert execute_single_instruction(FunkciaInstruction, [100, 54]) == [675]
