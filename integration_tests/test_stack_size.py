from random import randint, random

from ksplang.constants import MAX_INT, MIN_INT
from ksplang.execute import discover_instructions, instruction_notation_to_ids
from ksplang.executor import Executor

available_instructions = discover_instructions()

# sorting from ukol 3, https://ksp.mff.cuni.cz/h/ulohy/36/zadani3.html#task-36-3-4

instructions = "cs cs lensum cs funkcia cs cs pop pop cs cs lensum cs funkcia cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ lroll cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ lroll swap cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs lensum cs funkcia ++ ++ cs cs lensum cs funkcia ++ ++ ++ lroll swap pop cs cs lensum cs funkcia ++ ++ ++ ++ ++ u cs cs lensum cs funkcia cs ++ u cs j ++ cs bulkxor cs cs lensum cs funkcia ++ ++ cs cs lensum cs funkcia ++ ++ ++ lroll ++ cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ ++ lroll cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ lroll cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ lroll swap cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs lensum cs funkcia ++ ++ cs cs lensum cs funkcia ++ ++ ++ lroll swap pop cs cs lensum cs funkcia ++ ++ ++ ++ ++ u cs cs lensum cs funkcia cs ++ u cs j ++ cs bulkxor cs cs lensum cs funkcia ++ ++ ++ ++ ++ u cs cs lensum cs funkcia cs ++ u cs j ++ cs bulkxor cs cs lensum cs funkcia ++ ++ cs cs lensum cs funkcia ++ ++ ++ lroll and cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ ++ lroll ++ pop2 cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ lroll cs cs lensum cs funkcia ++ ++ ++ ++ ++ ++ ++ cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ lroll brz pop2 pop cs cs lensum cs funkcia cs ++ cs qeq u"


def test_sort():
    numintegers = randint(10, 100)
    # https://discord.com/channels/726020980107116585/782937605427560470/1208724596459835422
    # has to be able to sort between -2**63 and 2**63, as per ksplang developers
    # therefore we give something in between
    startstack = [randint(-(2**63), 2**63) for x in range(numintegers)]
    endstack = startstack[::]
    endstack.append(len(startstack))

    executor = Executor(
        instruction_notation_to_ids(instructions.split(" ")),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    assert endstack == executor.get_stack()
