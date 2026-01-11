from ksplang.execute import discover_instructions, execute_program

available_instructions = discover_instructions()

# the stack is not empty, there's always at least one number on it
# the stack should


def test_create_zero_one():
    startstack = [x for x in range(10)]
    endstack = startstack[::]
    endstack.append(0)

    result = execute_program(
        "CS CS CS ++ CS CS % pop2 pop2 pop2".split(" "),
        startstack,
        available_instructions,
    )
    # there should be a zero at the end
    assert result == endstack


def test_create_zero_two():
    startstack = [x for x in range(10)]
    endstack = startstack[::]
    endstack.append(0)

    result = execute_program(
        "CS CS lensum ++ CS %".split(" "), startstack, available_instructions
    )
    # there should be a zero at the end
    assert endstack == result
