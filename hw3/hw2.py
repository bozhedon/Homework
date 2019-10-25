def devider_generator(number):
    for n in range(1, number + 1):
        if number % n == 0:
            yield n


if __name__ == '__main__':
    deviders = devider_generator(1024)
    for i in deviders:
        print(i)
