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
        return " -> ".join(output)

    def empty(self):
        return self._head is None

if __name__ == '__main__':
    double_list = DoublyLinkedList()
    print(double_list)
