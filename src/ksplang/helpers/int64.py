def is_int64(value: int):
    return -9223372036854775808 <= value <= 9223372036854775807


# wrap a python value to int64 and preserve the sign
def to_int64(val: int) -> int:
    val = val & (2**64 - 1)
    if val & (1 << 63):
        val = val - (1 << 64)
    return val
