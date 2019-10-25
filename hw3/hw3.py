def row_generator(text):
    length = len(list(text))
    text.seek(0)
    while True:
        for i in range(length):
            yield text.readline().strip()
        text.seek(0)


if __name__ == '__main__':
    path_to_file = '/home/yan/Документы/python lessons/Homework/hw3/mytext'
    with open(path_to_file) as text:
        g = row_generator(text)
        for i, line in enumerate(g):
            if i > 10:
                break
            print(line)
