from enum import Enum


class NodeColor(Enum):
    RED = 0
    BLACK = 1


class Node():
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        self._parent = None
        self._color = NodeColor.BLACK

    def __str__(self):
        if self._color == NodeColor.RED:
            color = "R"
        else:
            color = "B"
        return f"{self._key}{color}"

    def insert(self, value):
        if self._key == value:
            return False
        elif self._key < value:
            if self._right:
                return self._right.insert(value)
            else:
                self._right = Node(value)
                self._right._parent = self
                return True
        else:
            if self._left:
                return self._left.insert(value)
            else:
                self._left = Node(value)
                self._left._parent = self
                return True


class RedBlackTree():
    def __init__(self):
        self._root = None

    def empty(self):
        return self._root is None

    def insert(self, value):
        if self.empty():
            self._root = Node(value)
            return True
        else:
            return self._root.insert(value)

if __name__ == '__main__':
    node = Node(1)
