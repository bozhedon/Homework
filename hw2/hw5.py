def is_valid(braces_string):
    lb, rb = 0, 0
    for i in range(len(braces_string)):
        if braces_string[i] == '(':
            lb += 1
        if braces_string[i] == ')':
            rb += 1
    return lb == rb


if __name__ == '__main__':
    braces = input()
    print(is_valid(braces))
