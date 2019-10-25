import time


def lru_cache(function):
    cache = {}

    def wrapper(*args, **kwargs):
        kw = frozenset(values for values in kwargs.values())
        if (args, kw) not in cache.keys():
            cache[args, kw] = function(*args, **kwargs)
            return cache[args, kw]
        else:
            return cache[args, kw]

    return wrapper


if __name__ == '__main__':
    @lru_cache
    def summa(a, b, c=0):
        time.sleep(1)
        return a + b + c


    print(summa(2, 1))
    print(summa(3, 1, c=4))
    print(summa(2, 2, c=2))
    print(summa(2, 2, c=2))