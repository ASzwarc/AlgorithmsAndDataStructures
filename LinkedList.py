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


class LinkedList():
    """
    Single linked list
    """
    def __init__(self):
        self._head = None

    def __str__(self):
        node = self.head
        output = []
        while node is not None:
            output.append(str(node))
            node = node._next
        return " -> ".join(output)

    def push(self, data):
        if self._head is None:
            self._head = Node(data)
        else:
            node = self._head
            while node._next is not None:
                node = node._next
            node._next = Node(data)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    print(linked_list)
