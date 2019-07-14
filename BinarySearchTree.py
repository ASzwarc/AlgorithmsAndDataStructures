"""
Implementation of binary search tree
"""


class Node():
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None


class BinarySearchTree():
    def __init__(self):
        self._root = None
