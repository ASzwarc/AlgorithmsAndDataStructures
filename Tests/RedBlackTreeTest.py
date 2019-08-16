import unittest
from DataStructures.RedBlackTree import Node, RedBlackTree, NodeColor


class TestNode(unittest.TestCase):
    def test_str(self):
        node = Node(1)
        self.assertEqual(str(node), "1B")
        node._color = NodeColor.RED
        self.assertEqual(str(node), "1R")

    def test_insert(self):
        node = Node(3)
        self.assertFalse(node.insert(3))
        self.assertTrue(node.insert(1))

    def test_get_inorder(self):
        node = Node(3)
        node.insert(1)
        node.insert(5)
        self.assertListEqual([(1, NodeColor.RED), (3, NodeColor.BLACK),
                              (5, NodeColor.RED)], node.get_inorder())
        node.insert(6)
        self.assertListEqual([(1, NodeColor.BLACK), (3, NodeColor.BLACK),
                              (5, NodeColor.BLACK), (6, NodeColor.RED)],
                             node.get_inorder())


class TestRedBlackTree(unittest.TestCase):
    def test_empty(self):
        rbt = RedBlackTree()
        self.assertTrue(rbt.empty())
