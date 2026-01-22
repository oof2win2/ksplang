from typing import TYPE_CHECKING, ClassVar

# fix for circular imports
if TYPE_CHECKING:
    from ksplang.executor import Executor


class BaseInstruction:
    notation: ClassVar[str]

    @staticmethod
    def execute(executor: "Executor") -> None:
        pass
