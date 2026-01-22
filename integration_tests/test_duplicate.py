from ksplang.execute import discover_instructions
from ksplang.executor import Executor

available_instructions = discover_instructions()


def test_duplicate():
    startstack = [5]
    endstack = [5, 5]

    executor = Executor(
        "CS CS lensum CS funkcia ++ ++ m CS CS lensum CS funkcia CS ++ CS qeq u CS CS lensum CS funkcia ++ bitshift CS CS lensum CS funkcia ++ ++ m CS CS lensum CS funkcia CS ++ CS qeq u CS CS lensum CS funkcia ++ bitshift pop2 CS CS lensum CS funkcia ++ ++ CS ++ ++ lroll m CS CS lensum CS funkcia ++ CS CS funkcia qeq CS CS lensum CS funkcia ++ bitshift pop2 CS CS lensum CS funkcia u ++ ++ ++ CS CS CS CS lensum CS funkcia CS ++ CS qeq u CS ++ CS lensum CS ++ ++ lroll CS funkcia u CS CS lensum CS funkcia ++ CS ++ ++ lroll CS CS lensum CS funkcia CS ++ CS qeq u CS CS funkcia u".split(
            " "
        ),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    # there should be a zero at the end
    assert endstack == executor.get_stack()
