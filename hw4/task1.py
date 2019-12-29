class Complex:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Complex(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)


if __name__ == '__main__':
    a = Complex(1, 2)
    b = Complex(2, 1)
    print('a + b = ', a + b)
    print('a - b = ', a - b)
    print('a * b = ', a * b)
