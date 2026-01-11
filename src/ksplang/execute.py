import importlib
import pkgutil
from logging import debug
from pathlib import Path
from typing import Sequence

from ksplang.instructions.base_instruction import BaseInstruction


def discover_instructions() -> Sequence[type[BaseInstruction]]:
    instructions = []
    instructions_path = Path(__file__).parent / "instructions"

    def walk_packages(path, prefix=""):
        for module_info in pkgutil.iter_modules([str(path)]):
            full_name = f"{prefix}{module_info.name}"
            yield full_name
            if module_info.ispkg:
                submodule_path = path / module_info.name
                yield from walk_packages(submodule_path, f"{full_name}.")

    for module_name in walk_packages(instructions_path):
        if module_name.endswith("_test") or module_name == "base_instruction":
            continue
        try:
            module = importlib.import_module(f"ksplang.instructions.{module_name}")
        except ImportError:
            continue
        for attr_name in dir(module):
            attr = getattr(module, attr_name)
            if (
                isinstance(attr, type)
                and issubclass(attr, BaseInstruction)
                and attr != BaseInstruction
            ):
                instructions.append(attr)

    return instructions


def execute_program(
    init_instructions: Sequence[str],
    init_stack: list[int],
    # sequence means all available instructions must extend from BaseInstruction
    available_instructions: Sequence[type[BaseInstruction]],
):
    instructions = init_instructions[::]
    stack = init_stack[::]
    for i, instruction in enumerate(instructions):
        ex = next(
            (ins for ins in available_instructions if ins.notation == instruction), None
        )
        if not ex:
            raise ValueError(f"Unknown instruction: {instruction}")
        ex.execute(stack)
        debug(f"Executed instruction {instruction} on stack {stack}")

    return stack
