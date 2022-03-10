import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, v):
        super(LoggableList, self).append(v)
        Loggable.log(self, str(v))


class ExtendedStack(list):
    def sum(self):
        self.append(self.pop(-1) + self.pop(-1))

    def sub(self):
        self.append(self.pop(-1) - self.pop(-1))

    def mul(self):
        self.append(self.pop(-1) * self.pop(-1))

    def div(self):
        self.append(self.pop(-1) // self.pop(-1))


def test1():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    ex_stack.div()
    assert ex_stack.pop() == 2
    ex_stack.sub()
    assert ex_stack.pop() == 6
    ex_stack.sum()
    assert ex_stack.pop() == 7
    ex_stack.mul()
    assert ex_stack.pop() == 2
    assert len(ex_stack) == 0
    print('TEST #1 OK')


def test2():
    a = LoggableList()
    a.append('msg 1')
    a.append('msg 2')
    print('TEST #2 OK')


if __name__ == "__main__":
    test1()
    test2()