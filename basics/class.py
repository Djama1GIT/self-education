class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity

    def can_add(self, v):
        return self.capacity - v >= 0

    def add(self, v):
        if self.can_add(v):
            self.capacity -= v
            return True
        else:
            return False


class Buffer:
    def __init__(self):
        self.arr = []

    def add(self, *a):
        self.arr += list(a)
        while len(self.arr) >= 5:
            print(sum(self.arr[:5]))
            self.arr = self.arr[5:]

    def get_current_part(self):
        return self.arr


def test():
    buf = Buffer()
    buf.add(1, 2, 3)
    buf.get_current_part()
    buf.add(4, 5, 6)
    buf.get_current_part()
    buf.add(7, 8, 9, 10)
    buf.get_current_part()
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    buf.get_current_part()


if __name__ == "__main__":
    test()