def row_generator(text):
    length = len(list(text))
    text.seek(0)
    while True:
        for i in range(length):
            yield text.readline().strip()
        text.seek(0)


def length_of_row_generator(text):
    for item in filter(lambda x: 'NOD19' in x, row_generator(text)):
        yield item


if __name__ == '__main__':
    path_to_file = '/home/yan/Документы/python lessons/Homework/hw3/mytext'
    with open(path_to_file) as text:
        g = length_of_row_generator(text)
        for i, length in enumerate(g):
            if i > 10:
                break
            print(length)
