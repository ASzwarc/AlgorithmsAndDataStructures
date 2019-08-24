import unittest
from datastructures.avl_tree import AVL, Node


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
        # GIVEN
        root = Node(5)
        root = root.insert(4)
        # WHEN
        root = root.insert(3)
        # THEN
        self.assertEqual([(3, 0), (4, 1), (5, 0)],
                         root.get_key_height_inorder())
        # case where new root has right child
        # GIVEN
        root = Node(5)
        root = root.insert(4)
        root = root.insert(3)
        # WHEN
        root = root.insert(4.5)
        # THEN
        self.assertEqual([(3, 0), (4, 2), (4.5, 0), (5, 1)],
                         root.get_key_height_inorder())

    def test_right_left_rotation(self):
        # GIVEN
        root = Node(-2)
        root = root.insert(1)
        # WHEN
        root = root.insert(0)
        # THEN
        self.assertEqual([(-2, 0), (0, 1), (1, 0)],
                         root.get_key_height_inorder())

    def test_left_right_rotation(self):
        # GIVEN
        root = Node(5)
        root = root.insert(3)
        # WHEN
        root = root.insert(4)
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
        avl.insert([1, 2, 3, 4])
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 0), (2, 2), (3, 1), (4, 0)])
        avl.insert([1, 2, 3, 4])
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 0), (2, 2), (3, 1), (4, 0)])
        avl.insert(5)
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 0), (2, 2), (3, 0), (4, 1), (5, 0)])
        avl.insert([6, 7])
        self.assertEqual(avl.get_key_height_inorder(),
                         [(1, 0), (2, 1), (3, 0), (4, 2), (5, 0), (6, 1),
                          (7, 0)])

    def test_print(self):
        avl = AVL()
        avl.insert([1, 2, 3, 4])
        self.assertEqual(avl.print_inorder(), "1 [0], 2 [2], 3 [1], 4 [0]")

    def test_find(self):
        # GIVEN
        avl = AVL()
        # THEN
        self.assertFalse(avl.find(0))
        # WHEN
        avl.insert(2)
        # THEN
        self.assertFalse(avl.find(0))
        # WHEN
        avl.insert(0)
        # THEN
        self.assertTrue(avl.find(0))

    def test_contains(self):
        # GIVEN
        avl = AVL()
        # THEN
        self.assertFalse(0 in avl)
        # WHEN
        avl.insert(0)
        # THEN
        self.assertTrue(0 in avl)

    def test_max(self):
        # GIVEN
        avl = AVL()
        # THEN
        self.assertEqual(avl.max(), None)
        # WHEN
        avl.insert([1, 2, 3, 4, 5])
        # THEN
        self.assertEqual(avl.max(), 5)

    def test_min(self):
        # GIVEN
        avl = AVL()
        # THEN
        self.assertEqual(avl.min(), None)
        # WHEN
        avl.insert([1, 2, 3, 4, 5])
        # THEN
        self.assertEqual(avl.min(), 1)

    def test_iteration(self):
        # GIVEN
        avl = AVL()
        # THEN
        result = []
        for element in avl:
            result.append(element)
        self.assertListEqual(result, [])
        # WHEN
        avl.insert([4, 6, 8, 2, 1])
        # THEN
        result = []
        for element in avl:
            result.append(element)
        self.assertListEqual(result, [(1, 0), (2, 1), (4, 0), (6, 2), (8, 0)])

    def test_delete(self):
        # GIVEN
        avl = AVL()
        # THEN deletion of node not in tree
        self.assertFalse(avl.delete(1))
        # GIVEN
        avl.insert([4, 6, 8, 2, 1])
        # WHEN delete node without children
        self.assertTrue(avl.delete(4))
        self.assertTrue(avl.delete(1))
        # THEN
        self.assertListEqual(avl.get_key_height_inorder(), [(2, 0), (6, 1),
                                                            (8, 0)])
        # GIVEN
        avl.insert([1, 4])
        # WHEN delete node without childred
        self.assertTrue(avl.delete(8))
        # THEN
        self.assertListEqual(avl.get_key_height_inorder(), [(1, 0), (2, 2),
                             (4, 0), (6, 1)])
        # WHEN delete node with 1 child
        self.assertTrue(avl.delete(6))
        # THEN
        self.assertListEqual(avl.get_key_height_inorder(), [(1, 0), (2, 1),
                             (4, 0)])
        # WHEN delete root node with 2 childred
        self.assertTrue(avl.delete(2))
        self.assertListEqual(avl.get_key_height_inorder(), [(1, 0), (4, 1)])
        # GIVEN
        avl.insert([5, 2, 0])
        self.assertListEqual(avl.get_key_height_inorder(), [(0, 0), (1, 1),
                             (2, 0), (4, 2), (5, 0)])
        # WHEN delete node with 2 children
        self.assertTrue(avl.delete(1))
        # THEN
        self.assertListEqual(avl.get_key_height_inorder(), [(0, 0), (2, 1),
                             (4, 2), (5, 0)])
