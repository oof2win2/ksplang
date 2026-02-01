from ksplang.execute import discover_instructions
from ksplang.executor import Executor

instructions = "rev ++ pop pop".split(" ")
exec = Executor(instructions, [1, 2, 3, 4, 2, 0], discover_instructions())

retval = 0
while retval == 0:
    retval = exec.step()
    print(
        exec.get_instruction_pointer(),
        exec.get_execution_direction(),
        exec.peek_rev_stack(),
    )
    input(f"Current stack is {exec.get_stack()}")
