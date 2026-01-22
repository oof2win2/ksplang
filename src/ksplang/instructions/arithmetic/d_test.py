from .d import GCDManyInstruction


def test_d_basic(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [12, 18, 2]) == [6]


def test_d_three_numbers(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [24, 36, 48, 3]) == [12]


def test_d_four_numbers(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [24, 36, 48, 60, 4]) == [12]


def test_d_single_number(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [25, 1]) == [25]


def test_d_with_zero(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [0, 5, 2]) == [5]


def test_d_with_negative(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [-12, 18, 2]) == [6]


def test_d_all_zeros(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [0, 0, 0, 3]) == [0]


def test_d_coprime(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [7, 13, 2]) == [1]


def test_d_preserves_stack_bottom(execute_single_instruction):
    assert execute_single_instruction(GCDManyInstruction, [99, 100, 12, 18, 2]) == [
        99,
        100,
        6,
    ]


def test_d_preserves_multiple_stack_bottom(execute_single_instruction):
    assert execute_single_instruction(
        GCDManyInstruction, [88, 99, 100, 24, 36, 48, 3]
    ) == [88, 99, 100, 12]
