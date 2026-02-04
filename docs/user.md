# User documentation

The main file, `src/ksplang/main.py`, is a program that accepts a command-line argument of a file input for the program to process. Initial stack variables are set as one line of stdin. The interpreter will execute the defined program, and print the final stack state to stdout.

Example usage:
```
uv run src/ksplang/main.py program.ksplang < input.txt
# input.txt
41 12
# program.ksplang
pop ++
```

The instruction set available within the ksplang language is available on the [ksplang website](https://ksp.mff.cuni.cz/h/ulohy/36/ksplang/).
