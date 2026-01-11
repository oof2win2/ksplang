# private fn, don't import
def __merge(first: list[int], second: list[int]) -> list[int]:
    result = []
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            result.append(first[i])
            i += 1
        else:
            result.append(second[j])
            j += 1
    # copy remaining items in the arrays that are "bigger than"
    result.extend(first[i:])
    result.extend(second[j:])
    return result


def mergesort(data: list[int]) -> list[int]:
    # base case
    if len(data) == 1:
        return data

    mid = len(data) // 2
    first = mergesort(data[mid:])
    second = mergesort(data[:mid])
    return __merge(first, second)
