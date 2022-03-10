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


def test():
    x = MoneyBox(10)
    x.add(5)
    x.add(5)
    print(x.can_add(1))


if __name__ == "__main__":
    test()