import sys

from ksplang.execute import (
    discover_instructions,
    execute_program,
    instruction_notation_to_ids,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: ./ksplang <program.ksplang>", file=sys.stderr)
        sys.exit(1)

    program_file = sys.argv[1]
    with open(program_file) as f:
        instructions = f.read().split()

    input_data = sys.stdin.read()
    stack = []
    for item in input_data.split():
        try:
            stack.append(int(item))
        except ValueError:
            stack.append(item)

    available_instructions = discover_instructions()

    result = execute_program(
        instruction_notation_to_ids(instructions), stack, available_instructions
    )

    print(" ".join(str(x) for x in result))


if __name__ == "__main__":
    main()
