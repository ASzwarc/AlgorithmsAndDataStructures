"""
Definition of LinkedList class
"""


class Node():
    """
    Linked list's node
    """
    def __init__(self, data: int):
        self._data = data
        self._next = None

    def __str__(self):
        return f"{self._data}"

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, data):
        self._next = Node(data)


class LinkedList():
    """
    Single linked list
    """
    def __init__(self):
        self._head = None

    def __str__(self):
        node = self._head
        output = []
        while node is not None:
            output.append(str(node))
            node = node.next
        return " -> ".join(output)

    def push(self, data: int):
        if self._head is None:
            self._head = Node(data)
        else:
            node = self._head
            while node.next is not None:
                node = node.next
            node.next = data


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    print(linked_list)
