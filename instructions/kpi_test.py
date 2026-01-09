from ..execute import execute_program
from .kpi import KPIInstruction


def test_kpi_first():
    instructions = [KPIInstruction.notation]
    available_instructions = [KPIInstruction]
    stack = [1, 2, 3, 4, 5]
    expected_stack = [3, 1, 4, 1, 5]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_kpi_second():
    instructions = [KPIInstruction.notation]
    available_instructions = [KPIInstruction]
    stack = [2, 2, 2, 2, 2]
    expected_stack = [2, 2, 4, 2, 2]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )


def test_kpi_third():
    instructions = [KPIInstruction.notation]
    available_instructions = [KPIInstruction]
    stack = [0, 1, 2, 3, 4]
    expected_stack = [0, 1, 2, 3, 5]
    assert (
        execute_program(instructions, stack, available_instructions) == expected_stack
    )
