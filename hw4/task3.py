class AffineTransform:
    def __init__(self, m, v):
        self.M = m
        self.v = v

    def transform(self, point):
        x = point[0]
        y = point[1]
        return x * self.M[0][0] + y * self.M[0][1] + self.v[0], x * self.M[1][0] + y * self.M[1][1] + self.v[1]

    def __add__(self, other):
        M1 = [[other.M[0][0] * self.M[0][0] + other.M[1][0] * self.M[0][1],
               other.M[0][1] * self.M[0][0] + other.M[1][1] * self.M[0][1]],
              [other.M[0][0] * self.M[1][0] + other.M[1][0] * self.M[1][1],
               other.M[0][1] * self.M[1][0] + other.M[1][1] * self.M[1][1]]]
        v1 = [other.v[0] * self.M[0][0] + other.v[1] * self.M[0][1] + self.v[0],
              other.v[0] * self.M[1][0] + other.v[1] * self.M[1][1] + self.v[1]]

        return AffineTransform(M1, v1)


if __name__ == '__main__':
    trans_1 = AffineTransform([[4, 1], [-3, 4]], [-6, 3])
    a = (2, 4)
    b = trans_1.transform(a)
    trans_2 = AffineTransform([[-1, -2], [2, 3]], [13, -5])
    c = trans_2.transform(b)
    trans_3 = trans_2 + trans_1
    d = trans_3.transform(a)

    print(a)
    print(b)
    print(c)
    print(d)
