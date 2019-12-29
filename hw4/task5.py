class linkedList():
    def __init__(self, *args):
        self.list = [*args]

    def __repr__(self):
        return 'Linked list:' + str(self.list)

    def next(self):
        return self.next()

    def add(self, el):
        return self.list.append(el)


class linkedListElement():
    def __init__(self):
        pass


a = linkedList(1, 2, 3)
a.add(4)
print(a)
