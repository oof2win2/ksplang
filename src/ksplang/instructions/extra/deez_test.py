from ksplang.instructions.extra.deez import DeezInstruction
from ksplang.instructions.stack.pop import PopInstruction


def test_deez(execute_multiple_instructions):
    # 2 instructions
    # 20: sum (creates 0 on an empty stack)
    # 9: ++ 0 -> 1
    # resulting stack: [1]
    # that is translated back into pop and added to the end of the program
    assert execute_multiple_instructions(
        [DeezInstruction, PopInstruction],
        [1, 2, 3, 9, 20, 2],
        [
            DeezInstruction.id,
        ],
    ) == [
        1,
        2,
    ]
