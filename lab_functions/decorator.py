import time


def lru(function):
    cache = {}

    def wrapper(*args, **kwargs):
        if args in cache.keys():
            print("Found in cache", args, kwargs)
            return cache[args]
        value = function(*args)
        cache[args] = value
        print("Added to cache", args, kwargs)
        return value

    return wrapper


@lru
def some_function(a, b, c=3):
    time.sleep(2)
    return a + b + c


t0 = time.time()
print(some_function(1, 2, c=3))
print(time.time() - t0)

t0 = time.time()
print(some_function(1, 2, c=3))
print(time.time() - t0)
