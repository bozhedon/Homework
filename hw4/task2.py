class Polynom:
    def __init__(self, *args):
        self.x = [x for x in args]

    def __add__(self, other):
        res = [x + y for x, y in zip(self.x, other.x)]
        if len(self.x) > len(other.x):
            res.extend([x for i, x in enumerate(self.x) if i >= len(other.x)])
        elif len(other.x) > len(self.x):
            res.extend([x for i, x in enumerate(other.x) if i >= len(self.x)])
        return Polynom(*res)

    def __sub__(self, other):
        res = [x - y for x, y in zip(self.x, other.x)]
        if len(self.x) > len(other.x):
            res.extend([x for i, x in enumerate(self.x) if i >= len(other.x)])
        elif len(other.x) > len(self.x):
            res.extend([- x for i, x in enumerate(other.x) if i >= len(self.x)])
        return Polynom(*res)

    def __mul__(self, other):
        multires = Polynom(*[0 for i in range(len(self.x))])
        for i, x in enumerate(other.x):
            res = [0 for n in range(i)]
            res.extend([y * x for y in self.x])
            multires = multires + Polynom(*res)
        return multires

    def __repr__(self):
        rep = ''
        first = False
        sign = ''
        if self.x[0] != 0:
            rep = str(self.x[0])
            first = True
        for i in range(1, len(self.x)):
            if self.x[i] == 0:
                continue
            if first:
                if self.x[i] > 0:
                    sign = ' + '
                else:
                    sign = ' - '
            first = True
            if i != 1:
                if abs(self.x[i]) == 1:
                    rep += '{}x^{}'.format(sign, str(i))
                else:
                    rep += '{}{}x^{}'.format(sign, str(abs(self.x[i])), str(i))
            else:
                if abs(self.x[i]) == 1:
                    rep += '{}x'.format(sign)
                else:
                    rep += '{}{}x'.format(sign, str(abs(self.x[i])))
        return rep


if __name__ == '__main__':
    a = Polynom(1, 2)
    b = Polynom(0, 1, 0, -5)
    print(a)
    print(b)
    print(a * b)
