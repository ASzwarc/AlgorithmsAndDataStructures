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

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

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
            node._height = max([child._height if child else -1 for child in
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

    def get_key_height_inorder(self):
        output = []
        if self.left:
            output = self.left.get_key_height_inorder()
        output.append((self.key, self._height))
        if self.right:
            output = output + self.right.get_key_height_inorder()
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
            return ", ".join(output)
        else:
            return "Tree is empty!!!"

    def get_key_height_inorder(self):
        if self._root:
            return self._root.get_key_height_inorder()
        else:
            return []


class TestAVL(unittest.TestCase):
    def test_insert_single_element(self):
        avl = AVL()
        self.assertTrue(avl.insert(1))
        self.assertEqual(avl.get_key_height_inorder(), [(1, 0)])
        self.assertFalse(avl.insert(1))
        self.assertEqual(avl.get_key_height_inorder(), [(1, 0)])

    def test_insert_list_of_elements(self):
        avl = AVL()
        avl.insert_list([1, 2, 3, 4])
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 3), (2, 2), (3, 1), (4, 0)])
        avl.insert_list([1, 2, 3, 4])
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 3), (2, 2), (3, 1), (4, 0)])

    def test_print(self):
        avl = AVL()
        avl.insert_list([1, 2, 3, 4])
        self.assertEqual(avl.print_inorder(), "1 [3], 2 [2], 3 [1], 4 [0]")

if __name__ == '__main__':
    unittest.main()
