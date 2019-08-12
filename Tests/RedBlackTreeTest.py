import unittest
from DataStructures.RedBlackTree import Node, RedBlackTree, NodeColor


class TestNode(unittest.TestCase):
    def test_str(self):
        node = Node(1)
        self.assertEqual(str(node), "1 BLACK")
        node._color = NodeColor.RED
        self.assertEqual(str(node), "1 RED")

    def test_insert(self):
        node = Node(1)
        self.assertFalse(node.insert(1))
        self.assertTrue(node.insert(2))


class TestRedBlackTree(unittest.TestCase):
    def test_empty(self):
        rbt = RedBlackTree()
        self.assertTrue(rbt.empty())
