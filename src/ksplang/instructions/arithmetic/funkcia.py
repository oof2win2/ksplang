from ksplang.instructions.base_instruction import BaseInstruction


def get_prime_factors(n: int) -> list[int]:
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    if n > 1:
        factors.append(n)
    return factors


class FunkciaInstruction(BaseInstruction):
    notation = "funkcia"

    @staticmethod
    def execute(stack: list[int]):
        first = stack.pop()
        second = stack.pop()

        ff = {}
        fs = {}
        for factor in get_prime_factors(first):
            if factor in ff:
                ff[factor] += 1
            else:
                ff[factor] = 1
        for factor in get_prime_factors(second):
            if factor in fs:
                fs[factor] += 1
            else:
                fs[factor] = 1

        all_factors = set(ff.keys()).union(fs.keys())
        result = {
            k: (fs.get(k, 0) + ff.get(k, 0))
            for k in all_factors
            if not (k in fs and k in ff)
        }
        if len(result) == 0:
            stack.append(0)
            return

        total = 1
        for factor, count in result.items():
            total *= factor**count
        stack.append(total % 1_000_000_007)

        return
