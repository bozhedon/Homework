# asd = map(lambda a: a[0] * a[1], zip(range(2, 5), range(3, 9, 2)))
# print(list(asd))


# Write `filter` expressions to convert the following inputs into the indicated outputs.
# ['12', '-2', '0'] --> ['12', '0']
print(list(filter(lambda x: int(x) >= 0, ['12', '-2', '0'])))
# ['hello', 'world'] --> ['world']
print(list(filter(lambda x: x[0] == 'w', ['hello', 'world'])))
# ['Stanford', 'Cal', 'UCLA'] --> ['Stanford']
print(list(filter(lambda x: len(x) > 4, ['Stanford', 'Cal', 'UCLA'])))
# range(20) --> [0, 3, 5, 6, 9, 10, 12, 15, 18]
print(list(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(20))))


