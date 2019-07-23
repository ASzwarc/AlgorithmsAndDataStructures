"""
Implementation of AVL tree
"""

class Node:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        self._height = 0

    def __str__(self):
        return f"{self._key} [{self._height}]"

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

class AVL:
    def __init__(self):
        self._root = None

if __name__ == '__main__':
    pass