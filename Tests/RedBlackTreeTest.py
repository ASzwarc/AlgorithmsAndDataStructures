import unittest
from DataStructures.RedBlackTree import Node, RedBlackTree


class TestNode(unittest.TestCase):
    pass


class TestRedBlackTree(unittest.TestCase):
    def test_empty(self):
        rbt = RedBlackTree()
        self.assertTrue(rbt.empty())
