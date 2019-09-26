def get_digit_sum(n):
    summa = 0
    if n < 0:
        n = - n
    while n > 0:
        summa = summa + n % 10
        n = n // 10
    return summa


if __name__ == '__main__':
    number = int(input('Введите число: '))
    get_digit_sum(number)
