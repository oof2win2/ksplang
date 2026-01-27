from ksplang.execute import discover_instructions
from ksplang.executor import Executor

instructions = "cs cs pop pop cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs lensum cs funkcia cs ++ cs qeq u cs cs lensum cs funkcia cs cs lensum cs funkcia ++ ++ ++ m cs cs ++ gcd ++ max cs cs % qeq cs cs cs ++ ++ qeq pop2 cs j ++ cs praise qeq qeq pop2 funkcia funkcia ++ % bitshift cs cs gcd cs ++ lroll cs u cs cs pop2 cs lensum m pop2 pop2 cs cs lensum cs funkcia ++ ++ ++ ++ ++ u cs cs lensum cs funkcia cs ++ u cs j ++ cs bulkxor cs cs lensum cs funkcia ++ ++ cs cs lensum cs funkcia ++ cs cs lensum cs funkcia ++ ++ lroll brz pop2 pop".split(
    " "
)
exec = Executor(instructions, [42, 42, 3], discover_instructions())

retval = 0
while retval == 0:
    exec.step()
    input(f"Current stack is {exec.get_stack()}")
