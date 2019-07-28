"""
Implementation of AVL tree
"""


class Node:
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        self._parent = None
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

    def recalculate_height_up(self):
        node = self._parent
        while node:
            node.height = max([child.height if child else -1 for child in
                               [node.left, node.right]]) + 1
            node = node._parent

    def insert(self, key):
        if self.key == key:
            return False
        elif key < self.key:
            if not self.left:
                new_node = Node(key)
                new_node._parent = self
                self.left = new_node
                new_node.recalculate_height_up()
                return True
            else:
                return self.left.insert(key)
        else:  # key > self.key
            if not self.right:
                new_node = Node(key)
                new_node._parent = self
                self.right = new_node
                new_node.recalculate_height_up()
                return True
            else:
                return self.right.insert(key)
        return False

    def print_inorder(self):
        output = []
        if self.left:
            output = self.left.print_inorder()
        output.append(str(self))
        if self.right:
            output = output + self.right.print_inorder()
        return output


class AVL:
    def __init__(self):
        self._root = None

    def insert(self, key):
        if not self._root:
            self._root = Node(key)
            return True
        else:
            return self._root.insert(key)

    def insert_list(self, iterable):
        for item in iterable:
            self.insert(item)

    def print_inorder(self):
        if self._root:
            output = self._root.print_inorder()
            print(" ".join(output))
        else:
            print("Tree is empty!!!")

if __name__ == '__main__':
    avl = AVL()
    avl.insert_list([3, 5, 6, 7, 8, -1])
    avl.print_inorder()
