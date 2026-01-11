def tetr(number: int, repetitions: int) -> int:
    if repetitions == 0:
        return 1
    if repetitions == 1:
        return number
    return number ** tetr(number, repetitions - 1)
