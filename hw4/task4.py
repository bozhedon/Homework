class FIFO:
    def __init__(self, *args):
        self.list = [*args]

    def __repr__(self):
        return str(self.list)

    def isEmpty(self):
        if self.list:
            return False
        else:
            return True

    def push(self, object):
        return self.list.append(object)

    def pop(self):
        return self.list.pop(0)


if __name__ == '__main__':
    ToDoList = FIFO()
    print(ToDoList.isEmpty())
    ToDoList.push('create')
    ToDoList.push('generate')
    ToDoList.push('loading')
    print(ToDoList)
    print(ToDoList.pop())
    print(ToDoList)