# Programmer documentation

## Base Program Layout

The interpreter itself is implemented in the `ksplang` package. It consists of several modules, each responsible for a specific aspect of the interpreter's functionality.
The main executor for the interpreter is in `ksplang/executor.py`. It accepts a list of instructions to execute, initial stack, and list of available instructions.
The main executor is responsible for executing the instructions and managing the stack with functions such as `stack_push`, `stack_pop`, etc.

All of the instructions are defined as `ksplang/instructions/<type>/<name>.py`. Each instruction is a Python class that implements the `execute` method, which takes the executor as the single argument. Each class must also define its `id` and `notation` attributes, so that they can be identified and executed by the executor.

Some helper functions (conversion functions for integers, mergesort, GCD, tetration, quadratic equation solver) are provided in `ksplang/helpers/`.

Integration tests, defined in `integration_tests/`, are used to verify the correctness of the interpreter's implementation. These are valid solutions to the problems defined in ksplang challenges, [here](https://ksp.mff.cuni.cz/h/ulohy/36/zadani2.html#task-36-2-4) and [here](https://ksp.mff.cuni.cz/h/ulohy/36/zadani3.html#task-36-3-4).

## Technical Details

Even though the interpreter is written in Python, all numbers must range between `2^63 - 1` and `2^63`, as per the ksplang specification. Numbers are represented with two's complement binary representation (the MSb is the sign bit). Helper functions are provided in `ksplang/helpers/int64.py`.

## Tests

To run tests, use `uvx pytest` (alias for `uv tool run pytest`). When ran in the project's root directory, it will execute any matching tests per the [default test discovery rules](https://docs.pytest.org/en/stable/explanation/goodpractices.html#test-discovery). Running in verbose (`uvx pytest -v`) will display all individual tests and whether they pass or not.

For testing instructions, `ksplang/instructions/conftest.py` provides fixtures for executing one instruction at a time, as well as executing multiple instructions in a row. Fixtures for executing a single step are not provided, as more complex cases require manual setup.
