from __future__ import annotations
from enum import Enum
from collections.abc import Iterable


class NodeColor(Enum):
    RED = 0
    BLACK = 1


class Node():
    def __init__(self, key):
        self._key = key
        self._left = None
        self._right = None
        self._parent = None
        self._color = NodeColor.BLACK

    def __str__(self):
        if self._color == NodeColor.RED:
            color = "R"
        else:
            color = "B"
        return f"{self._key}{color}"

    def _left_rotate(self, subtree_root: Node):
        print(f"Left rotate on {subtree_root}")

    def _left_right_rotate(self, subtree_root: Node):
        print(f"Left right rotate on {subtree_root}")

    def _right_rotate(self, subtree_root: Node):
        print(f"Right rotate on {subtree_root}")

    def _right_left_rotate(self, subtree_root: Node):
        print(f"Right left rotate on {subtree_root}")

    def _rebalance_tree(self):
        if self._parent is None:
            self._color = NodeColor.BLACK
            return
        if self._parent._parent and self._parent._parent._left is self._parent:
            uncle_node = self._parent._parent._right
        elif (self._parent._parent and
              self._parent._parent._right is self._parent):
            uncle_node = self._parent._parent._left
        else:
            print("_rebalance_tree: this shouldn't happen!")
            return

        if uncle_node._color == NodeColor.RED:
            self._parent._color = NodeColor.BLACK
            uncle_node._color = NodeColor.BLACK
            self._parent._parent._color = NodeColor.RED
            self._parent._parent._rebalance_tree()
        else:  # uncle is BLACK
            if self._parent._parent._left is self._parent:
                if self._parent._left is self:
                    # left left case
                    print(f"Left left case triggered by {self}")
                    self._right_rotate(self._parent)
                else:  # self is right child of parent
                    # left right case
                    print(f"Left right case triggered by {self}")
                    self._left_right_rotate(self._parent)
            else:  # parent is right child of grandparent
                if self._parent._right is self:
                    # right right case
                    print(f"Right right case triggered by {self}")
                    self._left_rotate(self._parent._parent)
                else:
                    # right left case
                    print(f"Right left case triggered by {self}")
                    self._right_left_rotate(self._parent)

    def insert(self, value):
        if self._key == value:
            return False
        elif self._key < value:
            if self._right:
                return self._right.insert(value)
            else:
                self._right = Node(value)
                self._right._color = NodeColor.RED
                self._right._parent = self
                if self._color == NodeColor.RED:
                    self._right._rebalance_tree()
                return True
        else:
            if self._left:
                return self._left.insert(value)
            else:
                self._left = Node(value)
                self._left._color = NodeColor.RED
                self._left._parent = self
                if self._color == NodeColor.RED:
                    self._left._rebalance_tree()
                return True

    def get_inorder(self):
        result = []
        if self._left:
            result = self._left.get_inorder()
        result.append((self._key, self._color))
        if self._right:
            result = result + self._right.get_inorder()
        return result

    def print_inorder(self):
        result = []
        if self._left:
            result = self._left.print_inorder()
        result.append(str(self))
        if self._right:
            result = result + self._right.print_inorder()
        return result


class RedBlackTree():
    """
    Class implementing Red Black Tree. It has to follow this rules:
    1. each node must be either RED or BLACK
    2. the root of the tree must be always be BLACK
    3. two RED nodes can never appear in a row within a tree; a RED node must
       always have a BLACK parent node and BLACK child nodes
    4. every branch path from the root node in the tree to a null pointer
       passes through the exact same number of BLACK nodes.
    """
    def __init__(self):
        self._root = None

    def empty(self):
        return self._root is None

    def insert(self, values):
        if isinstance(values, Iterable):
            ret_val = True
            for value in values:
                if self.empty():
                    self._root = Node(value)
                else:
                    ret_val = ret_val and self._root.insert(value)
            return ret_val
        else:
            if self.empty():
                self._root = Node(values)
                return True
            else:
                return self._root.insert(values)

    def get_inorder(self):
        if self.empty():
            return []
        else:
            return self._root.get_inorder()

    def print_inorder(self):
        if self.empty():
            return ""
        else:
            return ", ".join(self._root.print_inorder())

if __name__ == '__main__':
    node = Node(3)
    node.insert(1)
    node.insert(5)
    node.insert(6)
