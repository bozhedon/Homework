def is_valid(braces_string):
    n = 0
    for i in range(len(braces_string)):
        if braces_string[i] == '(':
            n += 1
        if braces_string[i] == ')':
            n -= 1
        if n < 0:
            return False
    return n == 0


if __name__ == '__main__':
    braces = input()
    print(is_valid(braces))
