"""
Implementation of AVL tree
"""
import unittest


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
                if node._right and node._right.get_balance() > 1:
                    node = node.right_left_rotation()
                else:
                    node = node.left_rotation()
            elif balance > 1:  # left heavy
                if node._left and node._left.get_balance() < -1:
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

    def print_inorder(self):
        output = []
        if self._left:
            output = self._left.print_inorder()
        output.append(str(self))
        if self._right:
            output = output + self._right.print_inorder()
        return output

    def get_key_height_inorder(self):
        output = []
        if self._left:
            output = self._left.get_key_height_inorder()
        output.append((self._key, self._height))
        if self._right:
            output = output + self._right.get_key_height_inorder()
        return output


class AVL:
    def __init__(self):
        self._root = None

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
            output = self._root.print_inorder()
            return ", ".join(output)
        else:
            return "Tree is empty!!!"

    def get_key_height_inorder(self):
        if self._root:
            return self._root.get_key_height_inorder()
        else:
            return []


class TestNode(unittest.TestCase):
    def test_left_rotation(self):
        # GIVEN
        root = Node(1)
        root = root.insert(2)
        # WHEN
        root = root.insert(3)
        # THEN
        self.assertEqual([(1, 0), (2, 1), (3, 0)],
                         root.get_key_height_inorder())
        # case where new root has left child
        # GIVEN
        root = Node(0)
        root = root.insert(2)
        root = root.insert(3)
        # WHEN
        root = root.insert(1)
        # THEN
        self.assertEqual([(0, 1), (1, 0), (2, 2), (3, 0)],
                         root.get_key_height_inorder())

    def test_right_rotation(self):
        root = Node(5)
        root.insert(4)
        root.insert(3)
        self.assertEqual([(3, 0), (4, 1), (5, 2)],
                         root.get_key_height_inorder())
        root = root.right_rotation()
        self.assertEqual([(3, 0), (4, 1), (5, 0)],
                         root.get_key_height_inorder())
        # case where new root has right child
        root = Node(5)
        root.insert(4)
        root.insert(3)
        root.insert(4.5)
        self.assertEqual([(3, 0), (4, 1), (4.5, 0), (5, 2)],
                         root.get_key_height_inorder())
        root = root.right_rotation()
        self.assertEqual([(3, 0), (4, 2), (4.5, 0), (5, 1)],
                         root.get_key_height_inorder())

    def test_right_left_rotation(self):
        # GIVEN
        root = Node(-2)
        root.insert(1)
        root.insert(0)
        self.assertEqual([(-2, 2), (0, 0), (1, 1)],
                         root.get_key_height_inorder())
        # WHEN
        root = root.right_left_rotation()
        # THEN
        self.assertEqual([(-2, 0), (0, 1), (1, 0)],
                         root.get_key_height_inorder())

    def test_left_right_rotation(self):
        # GIVEN
        root = Node(5)
        root.insert(3)
        root.insert(4)
        self.assertEqual([(3, 1), (4, 0), (5, 2)],
                         root.get_key_height_inorder())
        # WHEN
        root = root.left_right_rotation()
        # THEN
        self.assertEqual([(3, 0), (4, 1), (5, 0)],
                         root.get_key_height_inorder())


class TestAVL(unittest.TestCase):
    def test_insert_single_element(self):
        avl = AVL()
        avl.insert(1)
        self.assertEqual(avl.get_key_height_inorder(), [(1, 0)])
        avl.insert(1)
        self.assertEqual(avl.get_key_height_inorder(), [(1, 0)])

    def test_insert_list_of_elements(self):
        avl = AVL()
        avl.insert_list([1, 2, 3, 4])
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 0), (2, 2), (3, 1), (4, 0)])
        avl.insert_list([1, 2, 3, 4])
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 0), (2, 2), (3, 1), (4, 0)])
        avl.insert(5)
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 0), (2, 2), (3, 0), (4, 1), (5, 0)])
        # avl.insert_list([6, 7])
        # self.assertEqual(avl.get_key_height_inorder(),
        #                  [(1, 0), (2, 1), (3, 2), (4, 1), (5, 0)])

    def test_print(self):
        avl = AVL()
        avl.insert_list([1, 2, 3, 4])
        self.assertEqual(avl.print_inorder(), "1 [0], 2 [2], 3 [1], 4 [0]")

if __name__ == '__main__':
    unittest.main()
