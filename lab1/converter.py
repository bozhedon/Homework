def convert_fahr_to_cels(deg_fahr):
    return round((deg_fahr - 32) * 5 / 9, 2)


def convert():
    deg_fahr = float(input('Temperature F? '))
    print('It is {} degrees Celsius.'.format(convert_fahr_to_cels(deg_fahr)))


if __name__ == '__main__':
    convert()
