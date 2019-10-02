def get_partition(s):
    i, j = 0, 0
    part_list = []
    while i < len(s):
        i = s.rfind(s[j]) + 1
        if len(set(s[:i]) & set(s[i:])) == 0:
            part_list.append(s[:i])
            s = s[i:]
            i, j = 0, 0
        else:
            j = j + 1
    return part_list


if __name__ == '__main__':
    Str = input('S = ')
    print(get_partition(Str))
