from typing import TYPE_CHECKING, ClassVar

# fix for circular imports
if TYPE_CHECKING:
    from ksplang.executor import Executor


class BaseInstruction:
    id: ClassVar[int]
    notation: ClassVar[str]

    @staticmethod
    def execute(executor: "Executor") -> None:
        pass
