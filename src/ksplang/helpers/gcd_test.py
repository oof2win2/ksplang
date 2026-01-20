from .gcd import gcd


# some basics
def test_gcd_basics():
    assert gcd(12, 18) == 6
    assert gcd(24, 36) == 12
    assert gcd(100, 25) == 25
    assert gcd(7, 13) == 1
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5
    assert gcd(0, 0) == 0


def test_gcd_associativity():
    assert gcd(12, 18, 24) == gcd(12, gcd(18, 24))
    assert gcd(24, 36, 48) == gcd(gcd(24, 36), 48)
    assert gcd(100, 25, 50) == gcd(gcd(100, 25), 50)
    assert gcd(7, 13, 19) == gcd(gcd(7, 13), 19)
    assert gcd(0, 5, 10) == gcd(gcd(0, 5), 10)
    assert gcd(5, 0, 15) == gcd(gcd(5, 0), 15)
    assert gcd(0, 0, 0) == gcd(gcd(0, 0), 0)


def test_gcd_negative():
    assert gcd(-12, 18) == 6
    assert gcd(24, -36) == 12
    assert gcd(-100, 25) == 25
    assert gcd(7, -13) == 1
    assert gcd(0, -5) == 5
    assert gcd(-5, 0) == 5
    assert gcd(0, 0) == 0
