"""
Implementation of binary search tree
"""


class Node():
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def __str__(self):
        return f"{self._data}"

    def insert(self, data) -> bool:
        if data == self._data:
            return False
        elif data < self._data:
            if self._left is None:
                self._left = Node(data)
                return True
            else:
                self._left.insert(data)
        else:  # data > self._data
            if self._right is None:
                self._right = Node(data)
                return True
            else:
                self._right.insert(data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left_node):
        self._left = left_node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right_node):
        self._right = right_node


class BinarySearchTree():
    def __init__(self):
        self._root = None

    def empty(self):
        return self._root is None

    def insert(self, data) -> bool:
        if self.empty():
            self._root = Node(data)
            return True
        else:
            return self._root.insert(data)

if __name__ == '__main__':
    bst = BinarySearchTree()
    print(bst.insert(20))
    print(bst.insert(10))
    print(bst.insert(30))
