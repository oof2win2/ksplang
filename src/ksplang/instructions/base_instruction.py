from typing import ClassVar


class BaseInstruction:
    notation: ClassVar[str]

    @staticmethod
    def execute(stack: list[int]) -> None:
        pass
