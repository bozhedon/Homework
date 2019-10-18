from functools import reduce
import operator


def fact(n):
    """Return the factorial of a positive number."""
    return reduce(lambda x, y: operator.mul(x, y), range(1, n + 1))


print(fact(3))  # => 6
print(fact(7))  # => 5040
