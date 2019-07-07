"""
Definition of LinkedList class
"""


class Node():
    """
    Linked list's node
    """
    def __init__(self, data: int):
        self._data = data
        self._node = None


class LinkedList():
    """
    Single linked list
    """
    def __init__(self):
        self._head = None
