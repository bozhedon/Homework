def get_largest_perimiter(L):
    p = 0
    n = len(L)
    for i in range(n-2):
        for j in range(i + 1, n-1):
            for k in range(j + 1, n):
                a = float(L[i])
                b = float(L[j])
                c = float(L[k])
                if a + b > c and a + c > b and b + c > a and a + b + c > p:
                    p = a + b + c
    if p == 0:
        print('Невозможно составить треугольник')
        return None
    else:
        return p


if __name__ == '__main__':
    str = input('Введите числа: ')
    list = str.split()
    get_largest_perimiter(list)
