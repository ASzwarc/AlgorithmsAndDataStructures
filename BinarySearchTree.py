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
