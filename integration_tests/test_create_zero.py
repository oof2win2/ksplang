from ksplang.execute import discover_instructions, instruction_notation_to_ids
from ksplang.executor import Executor

available_instructions = discover_instructions()

# the stack is not empty, there's always at least one number on it
# the stack should


def test_create_zero_one():
    startstack = [x for x in range(10)]
    endstack = startstack[::]
    endstack.append(0)

    executor = Executor(
        instruction_notation_to_ids("CS CS CS ++ CS CS % pop2 pop2 pop2".split(" ")),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    # there should be a zero at the end
    assert endstack == executor.get_stack()


def test_create_zero_two():
    startstack = [x for x in range(10)]
    endstack = startstack[::]
    endstack.append(0)

    executor = Executor(
        instruction_notation_to_ids("CS CS CS ++ CS CS % pop2 pop2 pop2".split(" ")),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    # there should be a zero at the end
    assert endstack == executor.get_stack()


def test_create_zero_three():
    startstack = [x for x in range(10)]
    endstack = startstack[::]
    endstack.append(0)

    executor = Executor(
        instruction_notation_to_ids("CS CS lensum ++ CS %".split(" ")),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    result = executor.get_stack()

    # there should be a zero at the end
    assert endstack == result


def test_create_zero_four():
    startstack = [x for x in range(10)]
    endstack = startstack[::]
    endstack.append(0)

    executor = Executor(
        instruction_notation_to_ids("CS CS lensum CS funkcia".split(" ")),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    result = executor.get_stack()

    # there should be a zero at the end
    assert endstack == result


def test_create_zero_five():
    startstack = [x for x in range(10)]
    endstack = startstack[::]
    endstack.append(0)

    instructions = "CS CS ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ ++ bitshift".split(
        " "
    )

    executor = Executor(
        instruction_notation_to_ids(instructions),
        startstack,
        available_instructions,
    )
    executor.execute_program()
    result = executor.get_stack()

    # there should be a zero at the end
    assert endstack == result
