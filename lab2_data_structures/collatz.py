def collatz_len(n):
    l = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        l = l + 1
    return l


def max_collatz_len(n):
    max = 0
    for i in range(n):
        if collatz_len(i) > max:
            max = collatz_len(i)
    return max


print(collatz_len(13))  # => 10
print(max_collatz_len(1000))

# Challenge: Only attempt to solve these if you feel very comfortable with this material.
# print(max_collatz_len(1000000))
# print(max_collatz_len(100000000))
