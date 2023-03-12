class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root: Node = None

    def __find(self, node, parent, value) -> (Node, Node, bool):
        if node is None:
            return None, parent, False
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        elif value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        elif value == node.data:
            return node, parent, True

        return node, parent, False

    def append(self, node: Node) -> Node:
        if self.root is None:
            self.root = node
            return node

        s, p, fl_find = self.__find(self.root, None, node.data)
        if not fl_find and s:
            if node.data < s.data:
                s.left = node
            else:
                s.right = node

        return node

    @staticmethod
    def __del_leaf(s: Node, p: Node):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    @staticmethod
    def __del_one_child(s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __min(self, node, parent) -> (Node, Node):
        if node.left:
            return self.__min(node.left, node)

        return node, parent

    def remove(self, key: int):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    def show(self, node: Node):
        if node is None:
            return

        self.show(node.left)
        print(node.data, end=" ")
        self.show(node.right)

    @staticmethod
    def show_wide(node: Node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn


var = [10, 5, 7, 16, 13, 2, 20]

t = Tree()
for i in var:
    t.append(Node(i))

t.show(t.root)
print()
t.remove(5)
t.show_wide(t.root)
print()