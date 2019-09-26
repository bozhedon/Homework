def is_self_dividing(n):
    chislo = n
    if n < 0:
        n = -n
    while n > 0:
        if n % 10 != 0:
            if chislo % (n % 10) != 0:
                return False
        else:
            return False
        n = n // 10
    return True


if __name__ == '__main__':
    number = int(input('Введите число: '))
    is_self_dividing(number)
