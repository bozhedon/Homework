# Write `map` expressions to convert the following inputs into the indicated outputs.
# ['12', '-2', '0'] --> [12, -2, 0]
print(list(map(lambda x: int(x), ['12', '-2', '0'])))
# ['hello', 'world'] --> [5, 5]
print(list(map(lambda x: len(x), ['hello', 'world'])))
# ['hello', 'world']` --> ['olleh', 'dlrow']
print(list(map(lambda x: x[::-1], ['hello', 'world'])))
# range(2, 6) --> [(2, 4, 8), (3, 9, 27), (4, 16, 64), (5, 25, 125)]
print(list(map(lambda x: (x, x ** 2, x ** 3), range(2, 6))))
# zip(range(2, 5), range(3, 9, 2)) --> [6, 15, 28]
print(list(map(lambda x: x[0] * x[1], zip(range(2, 5), range(3, 9, 2)))))


# Write `filter` expressions to convert the following inputs into the indicated outputs.
# ['12', '-2', '0'] --> ['12', '0']
print(list(filter(lambda x: int(x) >= 0, ['12', '-2', '0'])))
# ['hello', 'world'] --> ['world']
print(list(filter(lambda x: x[0] == 'w', ['hello', 'world'])))
# ['Stanford', 'Cal', 'UCLA'] --> ['Stanford']
print(list(filter(lambda x: len(x) > 4, ['Stanford', 'Cal', 'UCLA'])))
# range(20) --> [0, 3, 5, 6, 9, 10, 12, 15, 18]
print(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(20))))
