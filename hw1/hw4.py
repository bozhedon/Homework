def is_prime(n):
    for i in range(2, int(n ** (1 / 2))+1):
        if n % i == 0:
            return False
    if n > 1:
        return True
    else:
        return False


if __name__ == '__main__':
    number = int(input('Введите число: '))
    is_prime(number)
