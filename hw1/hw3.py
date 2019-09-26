def get_is_power_of_two(n):
    if n < 0:
        return False
    while n > 0:
        if n % 2 == 0:
            n = n / 2
            if n == 1:
                return True
        else:
            return False


if __name__ == '__main__':
    number = int(input('Введите число: '))
    get_is_power_of_two(number)
