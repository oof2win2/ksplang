from logging import debug
from typing import Sequence

from ksplang.helpers.int64 import is_int64
from ksplang.instructions.base_instruction import BaseInstruction


class Executor:
    __instructions_to_execute: list[int]
    __stack: list[int]
    __available_instructions: list[type[BaseInstruction]]
    __instruction_pointer: int
    __execution_direction: int
    __count_executed_instructions: int
    __rev_stack: list[tuple[int, int]]

    def __init__(
        self,
        init_instructions: Sequence[int],
        init_stack: list[int],
        available_instructions: Sequence[type[BaseInstruction]],
    ):
        self.__instructions_to_execute = init_instructions
        self.__stack = init_stack
        self.__available_instructions = [None] * 50
        for ins in available_instructions:
            self.__available_instructions[ins.id] = ins
        self.__instruction_pointer = 0
        self.__execution_direction = 1
        self.__count_executed_instructions = 0
        self.__rev_stack = []

    def stack_len(self) -> int:
        return len(self.__stack)

    def stack_pop(self, index: int = -1) -> int:
        """
        Pops a value from the stack.
        @raises IndexError if the stack is empty
        """

        return self.__stack.pop(index)

    def stack_peek(self, index: int = -1) -> int:
        """
        Peeks at a value from the stack.
        @raises IndexError if the stack is empty
        """

        return self.__stack[index]

    def stack_push(self, value: int) -> None:
        """
        Pushes a value onto the stack.
        @raises ValueError if the value is not a 64-bit integer
        """

        if not is_int64(value):
            raise ValueError("Value is not a 64-bit integer")

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

        if not is_int64(value):
            raise ValueError("Value is not a 64-bit integer")

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

        if not all(is_int64(value) for value in values):
            raise ValueError("One or more values are not 64-bit integers")

        self.__stack.extend(values)

    def stack_reverse(self) -> None:
        """
        Reverses the stack.
        """
        self.__stack.reverse()

    def get_stack(self) -> list[int]:
        """
        Returns a copy of the current stack.
        """
        return self.__stack.copy()

    def get_instruction_pointer(self) -> int:
        """
        Returns the current instruction pointer.
        """
        return self.__instruction_pointer

    def set_instruction_pointer(self, value: int) -> None:
        """
        Sets the current instruction pointer.
        """
        self.__instruction_pointer = value

    def get_execution_direction(self) -> int:
        """
        Returns the current execution direction.
        """
        return self.__execution_direction

    def set_execution_direction(self, value: int) -> None:
        """
        Sets the current execution direction.
        """
        self.__execution_direction = value

    def get_program_size(self) -> int:
        """
        Returns the size of the program.
        """
        return len(self.__instructions_to_execute)

    def get_executed_instructions_count(self) -> int:
        """
        Returns the number of instructions executed.
        """
        return self.__count_executed_instructions

    def peek_rev_stack(self) -> tuple[int, int] | None:
        """
        Returns the rev stack.
        """
        return self.__rev_stack[-1] if len(self.__rev_stack) > 0 else None

    def append_rev_stack(self, rev: tuple[int, int]):
        """
        Appends a rev to the rev stack.
        """
        self.__rev_stack.append(rev)

    def pop_rev_stack(self) -> tuple[int, int]:
        """
        Pops a rev from the rev stack.
        """
        return self.__rev_stack.pop()

    def add_instruction(self, instruction_id: int):
        """
        Adds an instruction to the executor.
        """
        self.__instructions_to_execute.append(instruction_id)

    def execute_program(self):
        """
        Executes the program.
        """

        while True:
            if self.__instruction_pointer >= len(self.__instructions_to_execute):
                break
            if self.__instruction_pointer == -1:
                break
            lastrev = self.peek_rev_stack()
            if lastrev and lastrev[0] == self.__instruction_pointer:
                # reverse stack
                self.stack_reverse()
                # reverse the execution direction
                self.set_execution_direction(self.get_execution_direction() * -1)
                # set the IP to the return IP
                self.set_instruction_pointer(self.__rev_stack[-1][1])
                self.__rev_stack.pop()  # close the block
                continue

            instruction_id = self.__instructions_to_execute[self.__instruction_pointer]
            # print(
            #     f"Executing IP={self.__instruction_pointer}, instruction={instruction}, stack={self.__stack}"
            # )
            ex = self.__available_instructions[instruction_id]
            if not ex:
                raise ValueError(f"Unknown instruction: {instruction_id}")
            ex.execute(self)
            debug(
                f"Executed instruction {instruction_id} with new stack {self.__stack}"
            )
            self.__instruction_pointer += 1 * self.__execution_direction
            self.__count_executed_instructions += 1

    def step(self):
        """
        Executes one instruction.
        """

        if self.__instruction_pointer >= len(self.__instructions_to_execute):
            return 1
        if self.__instruction_pointer == -1:
            return 1
        lastrev = self.peek_rev_stack()
        if lastrev and lastrev[0] == self.__instruction_pointer:
            # reverse stack
            self.stack_reverse()
            # reverse the execution direction
            self.set_execution_direction(self.get_execution_direction() * -1)
            # set the IP to the return IP
            self.set_instruction_pointer(self.__rev_stack[-1][1])
            self.__rev_stack.pop()  # close the block

        instruction_id = self.__instructions_to_execute[self.__instruction_pointer]
        # print(
        #     f"Executing IP={self.__instruction_pointer}, instruction={instruction}, stack={self.__stack}"
        # )
        ex = self.__available_instructions[instruction_id]
        if not ex:
            raise ValueError(f"Unknown instruction: {instruction_id}")
        ex.execute(self)
        debug(f"Executed instruction {instruction_id} with new stack {self.__stack}")
        self.__instruction_pointer += 1 * self.__execution_direction
        self.__count_executed_instructions += 1
        return 0
