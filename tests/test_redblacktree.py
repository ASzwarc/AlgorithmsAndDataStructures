import unittest
from datastructures.red_black_tree import Node, RedBlackTree, NodeColor


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


class TestRotationAndRecoloring(unittest.TestCase):
    def test_left_left_case(self):
        root = Node(15)
        root._color = NodeColor.BLACK
        root._left = Node(7)
        root._left._color = NodeColor.RED
        root._right = Node(25)
        root._right._color = NodeColor.BLACK
        self.assertListEqual([(7, NodeColor.RED), (15, NodeColor.BLACK),
                              (25, NodeColor.BLACK)], root.get_inorder())
        root.insert(3)


class TestRedBlackTree(unittest.TestCase):
    def test_empty(self):
        rbt = RedBlackTree()
        self.assertTrue(rbt.empty())

    def test_get_inorder(self):
        rbt = RedBlackTree()
        self.assertListEqual([], rbt.get_inorder())

        rbt.insert(3)
        rbt.insert(1)
        rbt.insert(5)
        self.assertListEqual([(1, NodeColor.RED), (3, NodeColor.BLACK),
                              (5, NodeColor.RED)], rbt.get_inorder())

    def test_print_inorder(self):
        rbt = RedBlackTree()
        self.assertEqual("", rbt.print_inorder())

        rbt.insert(3)
        rbt.insert(1)
        rbt.insert(5)
        self.assertEqual("1R, 3B, 5R", rbt.print_inorder())

if __name__ == "__main__":
    unittest.main()
