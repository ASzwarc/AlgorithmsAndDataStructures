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

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node

    def left_rotation(self):
        pass

    def right_rotation(self):
        pass

    def left_right_rotation(self):
        pass

    def right_left_rotation(self):
        pass

    def insert(self, key):
        if self.key == key:
            return False
        elif key < self.key:
            if not self.left:
                new_node = Node(key)
                new_node.height = self.height + 1
                self.left = new_node
                # evaluate rotation
                return True
            else:
                return self.left.insert(key)
        else:  # key > self.key
            if not self.right:
                new_node = Node(key)
                new_node.height = self.height + 1
                self.right = new_node
                # evaluate rotation
                return True
            else:
                return self.right.insert(key)
        return False


class AVL:
    def __init__(self):
        self._root = None

if __name__ == '__main__':
    pass
