def get_is_beauty(n):
    summa = 0
    m = int(n)
    m2 = int(n)
    if m < 0:
        m = -m
        m2 = -m2
    while m > 0:
        summa = summa + m % 10
        m = m // 10
    if m2 % summa == 0:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    number = input('Введите число: ')
    get_is_beauty(number)
