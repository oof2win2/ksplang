# Zápočtový program

The specification of this program is an interpreter for the [ksplang](https://ksp.mff.cuni.cz/h/ulohy/36/ksplang/) programming language. The purpose of this interpreter is a final assignment.

## Specification

The specification of the program is to implement all of the instructions within the `ksplang` programming language, such that all tests on the website (examples from the instructions) and the solutions of various challenges run correctly.


## Installation

Install dependencies with `uv sync`

Example usage:
```
uv run src/ksplang/main.py program.ksplang < input.txt
# input.txt
41 12
# program.ksplang
pop ++
```

See more examples in [examples.md](docs/examples.md)


## Documentation

* [User documentation](docs/user.md)
* [Examples](docs/examples.md)
* [Programmer documentation](docs/programmer.md)
