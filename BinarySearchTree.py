"""
Implementation of binary search tree
"""


class Node():
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    def __str__(self):
        return f"{self._data}"

    def insert(self, data) -> bool:
        if data == self._data:
            return False
        elif data < self._data:
            if not self._left:
                self._left = Node(data)
                return True
            else:
                self._left.insert(data)
        else:  # data > self._data
            if not self._right:
                self._right = Node(data)
                return True
            else:
                self._right.insert(data)

    def find(self, value) -> bool:
        if value == self._data:
            return True
        elif value < self._data:
            if not self._left:
                return False
            else:
                return self._left.find(value)
        else:  # value > self._data
            if not self._right:
                return False
            else:
                return self._right.find(value)

    def inorder_traversal(self, root):
        result = []
        if root:
            result = self.inorder_traversal(root.left)
            result.append(str(root))
            result = result + self.inorder_traversal(root.right)
        return result

    def inorder_traversal_non_recursive(self, root):
        node_stack = []
        result = []
        current_node = root
        while current_node or len(node_stack) != 0:
            while current_node:
                node_stack.append(current_node)
                current_node = current_node.left

            current_node = node_stack.pop()
            result.append(str(current_node))
            current_node = current_node.right
        return result

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left_node):
        self._left = left_node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right_node):
        self._right = right_node


class BinarySearchTree():
    def __init__(self):
        self._root = None

    def __contains__(self, value) -> bool:
        if self.empty():
            return False
        else:
            return self._root.find(value)

    def empty(self):
        return self._root is None

    def insert(self, data) -> bool:
        if self.empty():
            self._root = Node(data)
            return True
        else:
            return self._root.insert(data)

    def min(self):
        if self.empty():
            return None
        else:
            current_node = self._root
            while current_node.left:
                current_node = current_node.left
            return current_node.data

    def max(self):
        if self.empty():
            return None
        else:
            current_node = self._root
            while current_node.right:
                current_node = current_node.right
            return current_node.data

    def print_inorder(self):
        if not self.empty():
            print(" ".join(self._root.inorder_traversal(self._root)))

    def print_inorder_non_recursive(self):
        print(" ".join(self._root.inorder_traversal_non_recursive(self._root)))

if __name__ == '__main__':
    bst = BinarySearchTree()
    print(bst.insert(20))
    print(bst.insert(10))
    print(bst.insert(30))
    print(bst.insert(-5))
    print(bst.insert(40))
    print(bst.insert(24))
    bst.print_inorder()
    bst.print_inorder_non_recursive()
    print(bst.min())
    print(bst.max())
    print(-5 in bst)
