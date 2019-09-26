def is_self_dividing(n):
    m = int(n)
    m2 = int(n)
    if m < 0:
        m = -m
        m2 = -m2
    while m > 0:
        if m % 10 != 0:
            if m2 % (m % 10) != 0:
                return False
        m = m // 10
    return False


if __name__ == '__main__':
    number = input('Введите число: ')
    is_self_dividing(number)
