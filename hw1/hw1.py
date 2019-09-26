def get_digit_sum(n):
    summa = 0
    m = int(n)
    if m < 0:
        m = - m
    n = str(m)
    for i in range(len(n)):
        summa = summa + m % 10
        m = m // 10
    return summa


if __name__ == '__main__':
    number = input('Введите число: ')
    get_digit_sum(number)
