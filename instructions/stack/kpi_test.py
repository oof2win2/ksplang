from .kpi import KPIInstruction


def test_kpi_inserts_sum_at_position(execute_single_instruction):
    assert execute_single_instruction(KPIInstruction, [1, 2, 3, 4, 5]) == [
        3,
        1,
        4,
        1,
        5,
    ]


def test_kpi_with_duplicates(execute_single_instruction):
    assert execute_single_instruction(KPIInstruction, [2, 2, 2, 2, 2]) == [
        2,
        2,
        4,
        2,
        2,
    ]


def test_kpi_with_zero_value(execute_single_instruction):
    assert execute_single_instruction(KPIInstruction, [0, 1, 2, 3, 4]) == [
        0,
        1,
        2,
        3,
        5,
    ]
