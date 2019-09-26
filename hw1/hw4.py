def is_prime(n):
    k = 0
    for i in range(2, n):
        if n % i == 0:
            return False
    if n > 0:
        return True
    else:
        return False


if __name__ == '__main__':
    number = int(input('Введите число: '))
    is_prime(number)
