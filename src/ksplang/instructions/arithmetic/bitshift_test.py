import pytest

from .bitshift import BitshiftInstruction


def test_bitshift(execute_single_instruction):
    # 2 << 1 is 4
    assert execute_single_instruction(BitshiftInstruction, [2, 1]) == [4]
    # 3 << 1 is 6
    assert execute_single_instruction(BitshiftInstruction, [3, 1]) == [6]


def test_bitshift_negative_num(execute_single_instruction):
    assert execute_single_instruction(BitshiftInstruction, [-1, 1]) == [-2]


# these results are from the REPL on the KSPlang website
# https://ksp.mff.cuni.cz/h/ulohy/36/ksplang/sim.html
def test_bitshift_overflow_positive(execute_single_instruction):
    assert execute_single_instruction(BitshiftInstruction, [1, 63]) == [
        -9223372036854775808
    ]


def test_bitshift_overflow_negative(execute_single_instruction):
    assert execute_single_instruction(BitshiftInstruction, [-1, 63]) == [
        -9223372036854775808
    ]


def test_bitshift_overflow_zero(execute_single_instruction):
    assert execute_single_instruction(BitshiftInstruction, [1, 64]) == [0]


def test_bitshift_negative_count(execute_single_instruction):
    with pytest.raises(ValueError):
        execute_single_instruction(BitshiftInstruction, [1, -2])
