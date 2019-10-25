def is_prime(num):
    if num <= 0:
        return False
    if num == 1:
        return False
    for i in range(2, int(num ** (1 / 2)) + 1):
        if num % i == 0:
            return False
    return True


def prime_generator():
    cursor = 0
    while True:
        if is_prime(cursor):
            yield cursor
        cursor += 1


# asd = prime_generator()
# for prime_number in asd:
#     if prime_number > 100:
#         break
#     print(prime_number)


def prime_with_seven_and_generator():
    prime_gen = prime_generator()
    for prime_num in prime_gen:
        if prime_num % 10 == 7:
            yield prime_num


asdf = prime_with_seven_and_generator()
for i, prime_num in enumerate(asdf):
    print(prime_num)
    if i > 100:
        break
