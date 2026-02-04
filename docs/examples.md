# Examples

More examples can be found in the `integration_tests` directory, which include a variety of programs.

## Basic I/O

Pop the topmost element from the stack, increment the current stack value.
```
uv run src/ksplang/main.py program.ksplang < input.txt
# input.txt
41 12
# program.ksplang
pop ++
```

## Create the value of 0 on the stack

Pop the topmost element from the stack, increment the current stack value.
```
uv run src/ksplang/main.py docs/examples/create_zero.ksplang < docs/examples/create_zero.in
```

## Sort `k` elements on the stack

The stack contains `k` elements and the value `k` at the top of the stack. The output of the program is the sorted stack.

```
uv run src/ksplang/main.py docs/examples/sort.ksplang < docs/examples/sort.in
```
