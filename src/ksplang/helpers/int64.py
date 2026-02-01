from ksplang.constants import MAX_INT, MIN_INT


def is_int64(value: int):
    return MIN_INT <= value <= MAX_INT


# wrap a python value to int64 and preserve the sign
def to_int64(val: int) -> int:
    val = val & (2**64 - 1)
    if val & (1 << 63):
        val = val - (1 << 64)
    return val
