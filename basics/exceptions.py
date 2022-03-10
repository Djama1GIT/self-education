class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, v):
        if v > 0:
            super().append(v)
        else:
            raise NonPositiveError


def test():
    try:
        x = PositiveList()
        x.append(2)
        x.append(3)
        try:
            x.append(-1)
        except NonPositiveError:
            pass
    finally:
        print("TEST OK")


if __name__ == "__main__":
    test()

