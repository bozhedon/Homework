def generate_pascal_row(row):
    if row:
        row.append(0)
        row_2 = row.copy()
        row_2.reverse()
        return [n_1 + n_2 for n_1, n_2 in zip(row, row_2)]
    else:
        return [1]


def print_pascal_triangle(n):
    row = []
    rows = []
    for i in range(n):
        row = generate_pascal_row(row)
        str_row = ""
        for r in row:
            str_row += str(r) + " "
        rows.append(str_row)
    for k in rows:
        print(k.center(len(str_row)))


print_pascal_triangle(20)
