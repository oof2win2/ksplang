from ksplang.execute import discover_instructions, instruction_notation_to_ids
from ksplang.executor import Executor

available_instructions = discover_instructions()

# the stack is not empty, there's always at least one number on it
# the stack should


def test_negate_one():
    startstack = [5]
    endstack = [-5]

    executor = Executor(
        instruction_notation_to_ids(
            "CS CS lensum CS funkcia ++ CS CS % qeq".split(" ")
        ),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    # there should be a zero at the end
    assert endstack == executor.get_stack()
