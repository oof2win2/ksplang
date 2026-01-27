from ksplang.execute import discover_instructions
from ksplang.executor import Executor

available_instructions = discover_instructions()

# the stack is not empty, there's always at least one number on it
# the stack should


def test_negate_one():
    startstack = [42, 42, 3]
    endstack = [42, 42, 3, 2, 1, 0]

    executor = Executor(
        "cs cs pop pop cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs lensum cs funkcia cs ++ cs qeq u cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs lensum cs funkcia ++ ++ ++ ++ ++ u cs cs lensum cs funkcia cs ++ u cs j ++ cs bulkxor cs cs lensum cs funkcia ++ ++ cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ lroll brz pop2 pop".split(
            " "
        ),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    # there should be a zero at the end
    assert endstack == executor.get_stack()
