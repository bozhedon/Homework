def get_is_beauty(n):
    summa = 0
    chislo = n
    if n < 0:
        n = -n
    while n > 0:
        summa = summa + n % 10
        n = n // 10
    if chislo % summa == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    number = int(input('Введите число: '))
    get_is_beauty(number)
