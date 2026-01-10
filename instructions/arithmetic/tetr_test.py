from ...helpers.tetr import tetr
from .tetr import TetrationInstruction


def test_tetr_calculates_tetration(execute_single_instruction):
    assert execute_single_instruction(TetrationInstruction, [3, 2]) == [tetr(2, 3)]


def test_tetr_larger_base(execute_single_instruction):
    assert execute_single_instruction(TetrationInstruction, [4, 2]) == [tetr(2, 4)]


def test_tetr_zero_exponent_returns_one(execute_single_instruction):
    assert execute_single_instruction(TetrationInstruction, [0, 2]) == [1]
