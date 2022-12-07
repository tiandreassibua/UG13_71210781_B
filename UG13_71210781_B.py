from NodeUG import Node
class BinaryTree:
    def __init__(self):
        self._root = Node(0, None)
        self._size = 0

    def add(self, data):
        if self._root._left is None and data % 2 != 0:
            self._root._left = Node(data, self._root)
        elif self._root._right is None and data % 2 == 0:
            self._root._right = Node(data, self._root)
        else:
            if data % 2 != 0:
                self._root._left.insert(data)
            else:
                self._root._right.insert(data)

    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    def nodes(self):
        self.inorder(self._root)

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left())
            print(node.getData(), end=' ')
            self.inorder(node.right())


tree = BinaryTree()
tree.add(5)
tree.add(4)
tree.add(3)
tree.add(9)
tree.add(8)
tree.add(6)
tree.add(7)
tree.add(11)
tree.add(10)
tree.nodes()