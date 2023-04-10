class Tree:
    def __init__(self, key, left, right):
        self.key: int = key
        self.left: Tree | None = left
        self.right: Tree | None = right
        self.depths = {}
        self.sorted_lst = [key]
        self.leaves = set()
        self.max = key
        self.prev_max = -1

    def __iadd__(self, other):
        if other.key not in self.leaves:
            self.add(other)
            self.leaves.add(other.key)
            if other.key > self.max:
                self.prev_max = 0 + self.max
                self.max = other.key
            elif other.key > self.prev_max:
                self.prev_max = other.key
        return self

    def add(self, other):
        if other.key < self.key:
            if self.left:
                self.left.add(other)
            else:
                self.left = other
        elif other.key > self.key:
            if self.right:
                self.right.add(other)
            else:
                self.right = other
        return self

    @staticmethod
    def make_tree(lst: list):
        root = Tree(lst[0], None, None)
        root.leaves.add(lst[0])
        for i in range(1, len(lst)):
            root += (Tree(lst[i], None, None))
        return root

    def __str__(self):
        return str(self.make_sorted_lst())

    def make_sorted_lst(self):
        self.sorted_lst = []
        self.__make_sorted_lst(self)
        return self.sorted_lst

    def __make_sorted_lst(self, _tree):
        if _tree.left:
            self.__make_sorted_lst(_tree.left)
        self.sorted_lst += [_tree.key]
        if _tree.right:
            self.__make_sorted_lst(_tree.right)

    def check_AVL(self, _tree):
        if not _tree:
            return True
        return abs(self.height(_tree.right) - self.height(_tree.left)) <= 1 and self.check_AVL(_tree.left)\
               and self.check_AVL(_tree.right)

    def height(self, _tree):
        if not _tree:
            return 0
        return 1 + max(self.height(_tree.left), self.height(_tree.right))


tree = Tree.make_tree(list(map(int, input().split())))

print("YES" if tree.check_AVL(tree) else "NO")
