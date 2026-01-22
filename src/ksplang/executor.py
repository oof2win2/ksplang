from logging import debug
from typing import Sequence

from ksplang.helpers.int64 import is_int64
from ksplang.instructions.base_instruction import BaseInstruction


class Executor:
    __instructions_to_execute: Sequence[str]
    __stack: list[int]
    __available_instructions: Sequence[type[BaseInstruction]]

    def __init__(
        self,
        init_instructions: Sequence[str],
        init_stack: list[int],
        available_instructions: Sequence[type[BaseInstruction]],
    ):
        self.__instructions_to_execute = init_instructions
        self.__stack = init_stack
        self.__available_instructions = available_instructions

    def stack_len(self) -> int:
        return len(self.__stack)

    def stack_pop(self, index: int = -1) -> int:
        """
        Pops a value from the stack.
        @raises IndexError if the stack is empty
        """

        return self.__stack.pop(index)

    def stack_push(self, value: int) -> None:
        """
        Pushes a value onto the stack.
        @raises ValueError if the value is not a 64-bit integer
        """

        # if not is_int64(value):
        #     raise ValueError("Value is not a 64-bit integer")

        self.__stack.append(value)

    def stack_get(self, index: int) -> int:
        """
        Gets a value at a specific index in the stack.
        @raises IndexError if the index is out of range
        """

        return self.__stack[index]

    def stack_set(self, index: int, value: int) -> None:
        """
        Sets a value at a specific index in the stack.
        @raises IndexError if the index is out of range
        @raises ValueError if the value is not a 64-bit integer
        """

        # if not is_int64(value):
        #     raise ValueError("Value is not a 64-bit integer")

        self.__stack[index] = value

    def stack_clear(self) -> None:
        """
        Clears the stack.
        """

        self.__stack.clear()

    def stack_extend(self, values: list[int]) -> None:
        """
        Extends the stack with a list of values.
        @raises ValueError if any value is not a 64-bit integer
        """

        # if not all(is_int64(value) for value in values):
        #     raise ValueError("One or more values are not 64-bit integers")

        self.__stack.extend(values)

    def get_stack(self) -> list[int]:
        """
        Returns a copy of the current stack.
        """
        return self.__stack.copy()

    def execute_program(self):
        """
        Executes the program.
        """

        for i, instruction in enumerate(self.__instructions_to_execute):
            ex = next(
                (
                    ins
                    for ins in self.__available_instructions
                    if ins.notation == instruction
                ),
                None,
            )
            if not ex:
                raise ValueError(f"Unknown instruction: {instruction}")
            ex.execute(self)
            debug(f"Executed instruction {instruction} with new stack {self.__stack}")

    def step(self):
        """
        Takes one step through the program
        """

        if len(self.__instructions_to_execute) == 0:
            print("Program finished")
            return 1

        instruction = self.__instructions_to_execute.pop(0)
        ex = next(
            (
                ins
                for ins in self.__available_instructions
                if ins.notation == instruction
            ),
            None,
        )
        if not ex:
            raise ValueError(f"Unknown instruction: {instruction}")
        ex.execute(self)
        debug(f"Executed instruction {instruction} with new stack {self.__stack}")
        return 0
