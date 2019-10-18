def gcd(a, b):
    if a > b:
        a, b = b, a
    for i in reversed(range(a + 1)):
        if i == 0:
            print(b)
            return b
        if b % i == 0 and a % i == 0:
            print(i)
            return i


gcd(10, 25)  # => 5
gcd(14, 15)  # => 1
gcd(3, 9)  # => 3
gcd(1, 1)  # => 1
gcd(100, 0)
gcd(100, 25)