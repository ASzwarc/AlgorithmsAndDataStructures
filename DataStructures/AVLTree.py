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

    def left_rotation(self):
        new_root = self._right
        new_root._parent = self._parent
        self._parent = new_root
        if new_root._left:
            self._right = new_root._left
            new_root._left._parent = self._right
        else:
            self._right = None
        new_root._left = self
        if new_root._parent is not None:
            if new_root._parent._left is self:
                new_root._parent._left = new_root
            if new_root._parent._right is self:
                new_root._parent._right = new_root
        self.recalculate_height_up()
        return new_root

    def right_rotation(self):
        new_root = self._left
        new_root._parent, self._parent = self._parent, new_root
        if new_root._right:
            self._left = new_root._right
            new_root._right._parent = self._left
        else:
            self._left = None
        new_root._right = self
        if new_root._parent is not None:
            if new_root._parent._left is self:
                new_root._parent._left = new_root
            if new_root._parent._right is self:
                new_root._parent._right = new_root
        self.recalculate_height_up()
        return new_root

    def left_right_rotation(self):
        new_root = self._left.left_rotation()
        self._left = new_root
        return self.right_rotation()

    def right_left_rotation(self):
        new_root = self._right.right_rotation()
        self._right = new_root
        return self.left_rotation()

    def recalculate_height_up(self):
        node = self
        while node:
            node._height = max([child._height if child else -1 for child in
                               [node._left, node._right]]) + 1
            node = node._parent

    def get_balance(self):
        left_height, right_height = -1, -1
        if self._left:
            left_height = self._left._height
        if self._right:
            right_height = self._right._height
        return left_height - right_height

    def align_subtree(self):
        node = self._parent
        if node is None:
            return self
        while node:
            balance = node.get_balance()
            if balance < -1:  # right heavy
                if node._right and node._right.get_balance() >= 1:
                    node = node.right_left_rotation()
                else:
                    node = node.left_rotation()
            elif balance > 1:  # left heavy
                if node._left and node._left.get_balance() <= -1:
                    node = node.left_right_rotation()
                else:
                    node = node.right_rotation()
            if node._parent is None:
                return node
            else:
                node = node._parent
        return node

    def insert(self, key):
        if self._key == key:
            return None
        elif key < self._key:
            if not self._left:
                new_node = Node(key)
                new_node._parent = self
                self._left = new_node
                new_node.recalculate_height_up()
                return new_node.align_subtree()
            else:
                return self._left.insert(key)
        else:  # key > self.key
            if not self._right:
                new_node = Node(key)
                new_node._parent = self
                self._right = new_node
                new_node.recalculate_height_up()
                return new_node.align_subtree()
            else:
                return self._right.insert(key)
        return None

    def get_inorder(self):
        output = []
        if self._left:
            output = self._left.get_inorder()
        output.append(str(self))
        if self._right:
            output = output + self._right.get_inorder()
        return output

    def get_key_height_inorder(self):
        output = []
        if self._left:
            output = self._left.get_key_height_inorder()
        output.append((self._key, self._height))
        if self._right:
            output = output + self._right.get_key_height_inorder()
        return output

    def find(self, key):
        if key == self._key:
            return self
        elif key < self._key and self._left:
            return self._left.find(key)
        elif key > self._key and self._right:
            return self._right.find(key)
        else:
            return None


class AVL:
    def __init__(self):
        self._root = None

    def __contains__(self, data):
        return self.find(data)

    def insert(self, key) -> bool:
        if not self._root:
            self._root = Node(key)
            return True
        else:
            node = self._root.insert(key)
            if node and node._parent is None:
                self._root = node

    def insert_list(self, iterable):
        for item in iterable:
            self.insert(item)

    def print_inorder(self):
        if self._root:
            output = self._root.get_inorder()
            return ", ".join(output)
        else:
            return "Tree is empty!!!"

    def get_key_height_inorder(self):
        if self._root:
            return self._root.get_key_height_inorder()
        else:
            return []

    def find(self, key) -> bool:
        if not self._root:
            return False
        else:
            return bool(self._root.find(key))
