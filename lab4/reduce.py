def generate_fibs():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

g = generate_fibs()
print(next(g))