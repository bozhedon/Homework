def get_is_power_of_two(n):
    if n < 0:
        print('False')
        return 0
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            if n == 1:
                print('True')
                return 0
        else:
            print('False')
            return 0


if __name__ == '__main__':
    number = int(input('Введите число: '))
    get_is_power_of_two(number)
