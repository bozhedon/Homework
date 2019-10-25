import itertools
import operator


def dot_product(u, v):
    """Return the dot product of two equal-length lists of numbers."""
    return sum(list(itertools.starmap(operator.mul, itertools.zip_longest(u, v, fillvalue=0))))


print(dot_product([1, 3, 5,], [2, 4, 6]))
