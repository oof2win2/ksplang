def gcd(*numbers: int) -> int:
    # shouldn't happen
    if len(numbers) == 0:
        raise ValueError("gcd() requires at least one number")
    if len(numbers) == 1:
        return abs(numbers[0])

    # base case, two numbers
    if len(numbers) == 2:
        a, b = numbers
        while b:
            a, b = b, a % b
        return abs(a)

    # gcd is associative -> gcd(a, b, c) = gcd(gcd(a, b), c)
    return gcd(numbers[0], gcd(*numbers[1:]))
