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
            color = "RED"
        else:
            color = "BLACK"
        return f"{self._key} {color}"


class RedBlackTree():
    def __init__(self):
        self._root = None

    def empty(self):
        return self._root is None

if __name__ == '__main__':
    node = Node(1)
