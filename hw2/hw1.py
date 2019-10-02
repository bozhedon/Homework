def number_of_matches(j, s):
    # n = 0
    # for value in set(j) & set(s):
    #     n += list(s).count(value)
    # return n

    # more pythonic way, but slower ??
    return len([l for l in list(s) if l in set(j)])


if __name__ == '__main__':
    str1 = input('Введите J: ')
    str2 = input('Введите S: ')
    print(number_of_matches(str1, str2))
