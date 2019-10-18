def fizzbuzz(n):
    sum = 0
    """Returns the sum of all numbers less than n divisible by 3 or 5."""
    for m in [x for x in range(n) if x % 3 == 0 or x % 5 == 0]:
        sum = sum + m
    return sum


print(fizzbuzz(41))  # => 408
print(fizzbuzz(1001))
