from math import sqrt


def solve_qeq(a: int, b: int, c: int) -> list[int]:
    if a == 0 and b == 0:
        # c == 0 equation, infinite solutions
        if c == 0:
            raise ValueError("The equation is indeterminate.")
        # for c != 0, there are no solutions
        return []

    if a == 0:
        # linear equation
        sol = -c / b
        if sol.is_integer():
            return [int(sol)]
        return []

    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        # no real solutions
        return []
    discrim_sqrt = sqrt(discriminant)

    if discriminant == 0:
        # one real solution
        sol = -b / (2 * a)
        if sol.is_integer():
            return [int(sol)]
        return []

    sols = [
        int((-b + discrim_sqrt) / (2 * a)),
        int((-b - discrim_sqrt) / (2 * a)),
    ]

    if sols[0] == sols[1]:
        return [sols[0]]

    sols.sort()
    return [sols[0], sols[1]]
