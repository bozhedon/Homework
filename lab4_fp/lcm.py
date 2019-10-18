from functools import reduce
from math import gcd


def lcm(*nums):
    """Return the least common multiple of an arbitrary collection of numbers."""
    return reduce(lambda x, y: (x * y) // gcd(x, y), nums, 1)


print(lcm(3, 5))
print(lcm(41, 106, 12))
print(lcm(1, 2, 6, 24, 120, 720))
print(lcm(3))
print(lcm())
