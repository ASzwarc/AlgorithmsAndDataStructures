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

    def test_find(self):
        node = Node(3)
        node.insert(1)
        node.insert(0)
        node.insert(5)
        node = node._parent
        self.assertTrue(node.find(0))
        self.assertTrue(node.find(5))
        self.assertFalse(node.find(10))


class TestRotationAndRecoloring(unittest.TestCase):
    def test_left_left_case(self):
        root = Node(15)
        root._color = NodeColor.BLACK
        root._left = Node(7)
        root._left._color = NodeColor.RED
        root._left._parent = root
        root._right = Node(25)
        root._right._color = NodeColor.BLACK
        root._right._parent = root
        self.assertListEqual([(7, NodeColor.RED), (15, NodeColor.BLACK),
                              (25, NodeColor.BLACK)], root.get_inorder())
        root.insert(3)
        root = root._parent
        self.assertListEqual([(3, NodeColor.RED), (7, NodeColor.BLACK),
                              (15, NodeColor.RED), (25, NodeColor.BLACK)],
                             root.get_inorder())

    def test_right_right_case(self):
        root = Node(15)
        root._color = NodeColor.BLACK
        root._left = Node(7)
        root._left._color = NodeColor.BLACK
        root._left._parent = root
        root._right = Node(25)
        root._right._color = NodeColor.RED
        root._right._parent = root
        self.assertListEqual([(7, NodeColor.BLACK), (15, NodeColor.BLACK),
                              (25, NodeColor.RED)], root.get_inorder())
        root.insert(27)
        root = root._parent
        self.assertListEqual([(7, NodeColor.BLACK), (15, NodeColor.RED),
                              (25, NodeColor.BLACK), (27, NodeColor.RED)],
                             root.get_inorder())

    def test_left_right_case(self):
        root = Node(15)
        root._color = NodeColor.BLACK
        root._left = Node(7)
        root._left._color = NodeColor.RED
        root._left._parent = root
        root._right = Node(25)
        root._right._color = NodeColor.BLACK
        root._right._parent = root
        self.assertListEqual([(7, NodeColor.RED), (15, NodeColor.BLACK),
                              (25, NodeColor.BLACK)], root.get_inorder())
        root.insert(8)
        root = root._parent
        self.assertListEqual([(7, NodeColor.RED), (8, NodeColor.BLACK),
                              (15, NodeColor.RED), (25, NodeColor.BLACK)],
                             root.get_inorder())

    def test_right_left_case(self):
        root = Node(15)
        root._color = NodeColor.BLACK
        root._left = Node(7)
        root._left._color = NodeColor.BLACK
        root._left._parent = root
        root._right = Node(25)
        root._right._color = NodeColor.RED
        root._right._parent = root
        self.assertListEqual([(7, NodeColor.BLACK), (15, NodeColor.BLACK),
                              (25, NodeColor.RED)], root.get_inorder())
        root.insert(24)
        root = root._parent
        self.assertListEqual([(7, NodeColor.BLACK), (15, NodeColor.RED),
                              (24, NodeColor.BLACK), (25, NodeColor.RED)],
                             root.get_inorder())


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

    def test_insert(self):
        rbt = RedBlackTree()
        rbt.insert([10, 20, 30])
        self.assertListEqual([(10, NodeColor.RED), (20, NodeColor.BLACK),
                              (30, NodeColor.RED)], rbt.get_inorder())
        rbt.insert(15)
        self.assertListEqual([(10, NodeColor.BLACK), (15, NodeColor.RED),
                              (20, NodeColor.BLACK), (30, NodeColor.BLACK)],
                             rbt.get_inorder())

    def test_max(self):
        rbt = RedBlackTree()
        rbt.insert([10, 20, 56, 78])
        self.assertListEqual([(10, NodeColor.BLACK), (20, NodeColor.BLACK),
                              (56, NodeColor.BLACK), (78, NodeColor.RED)],
                             rbt.get_inorder())
        self.assertEqual(rbt.max(), 78)

    def test_min(self):
        rbt = RedBlackTree()
        rbt.insert([0, 20, 1, 5])

        self.assertListEqual([(0, NodeColor.BLACK), (1, NodeColor.BLACK),
                              (5, NodeColor.RED), (20, NodeColor.BLACK)],
                             rbt.get_inorder())
        self.assertEqual(rbt.min(), 0)

    def test_find(self):
        rbt = RedBlackTree()
        rbt.insert([3, 1, 0, 5])
        self.assertTrue(rbt.find(0))
        self.assertTrue(rbt.find(5))
        self.assertFalse(rbt.find(10))


if __name__ == "__main__":
    unittest.main()
