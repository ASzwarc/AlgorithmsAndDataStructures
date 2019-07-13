"""
Implementation of doubly linked list
"""


class Node():
    def __init__(self, data):
        self._data = data
        self._prev = None
        self._next = None

    def __str__(self):
        return f"{self._data}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, node):
        self._prev = node


class DoublyLinkedList():
    def __init__(self):
        self._head = None

    def __str__(self):
        current_node = self._head
        output = []
        while current_node is not None:
            output.append(str(current_node))
            current_node = current_node._next
        return " <-> ".join(output)

    def empty(self):
        return self._head is None

    def push_back(self, node):
        if self.empty():
            self._head = Node(node)
        else:
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next
            new_node = Node(node)
            current_node.next = new_node
            new_node.prev = current_node

    def push_front(self, node):
        if self.empty():
            self._head = Node(node)
        else:
            current_node = self._head
            new_node = Node(node)
            new_node.next = current_node
            current_node.prev = new_node
            self._head = new_node

    def pop_back(self):
        if self.empty():
            return None
        else:
            current_node = self._head
            while current_node.next is not None:
                current_node = current_node.next
            ret_val = current_node.data
            current_node.prev.next = None
            return ret_val

    def pop_front(self):
        if self.empty():
            return None
        else:
            current_node = self._head
            ret_val = current_node.data
            if current_node.next is None:
                self._head = None
            else:
                self._head = current_node.next
                current_node.next.prev = None
            return ret_val

if __name__ == '__main__':
    double_list = DoublyLinkedList()
    double_list.push_front(-10)
    double_list.push_back(0)
    double_list.push_back(1)
    print(double_list)
    double_list.push_front(-1)
    double_list.push_front(-2)
    print(double_list)
    print(double_list.pop_back())
    print(double_list)
    print(double_list.pop_front())
    print(double_list)
