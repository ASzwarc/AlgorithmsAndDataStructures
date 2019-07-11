"""
Definition of LinkedList class
"""


class Node():
    """
    Linked list's node
    """
    def __init__(self, data):
        self._data = data
        self._next = None

    def __str__(self):
        return f"{self._data}"

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, node):
        self._next = node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value


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

    def push_back(self, data):
        node = self._head
        if node is None:
            self._head = Node(data)
        else:
            while node.next is not None:
                node = node.next
            node.next = Node(data)

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self._head
        self._head = new_node

    def pop_front(self):
        if self.empty():
            return None
        current_node = self._head
        ret_val = current_node.data
        if current_node.next is None:
            current_node = None
        else:
            self._head = current_node.next
        return ret_val

    def pop_back(self):
        if self.empty():
            return None
        current_node = self._head
        if current_node.next is None:
            ret_val = current_node.data
            current_node = None
        else:
            while current_node.next.next is not None:
                current_node = current_node.next
            ret_val = current_node.next.data
            current_node.next = None
        return ret_val

    def insert(self, pos, data) -> bool:
        if self.empty():
            return False
        else:
            current_node = self._head
            while (current_node.next is not None and current_node.data != pos):
                current_node = current_node.next
            if current_node.data == pos:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return True
            else:  # reached end of list and there is no element 'pos'
                return False

    def remove(self, pos) -> bool:
        def evaluate_last_element(current_node):
            if current_node.data != pos:
                return False
            else:
                self.pop_back()
                return True

        if self.empty():
            return False
        else:
            current_node = self._head
            if current_node.data == pos:
                self.pop_front()
                return True
            if current_node.next is None:
                return evaluate_last_element(current_node)
            else:
                while (current_node.next.next is not None and
                       current_node.next.data != pos):
                    current_node = current_node.next
                if current_node.next.data == pos:
                    new_end = current_node.next.next
                    current_node.next = new_end
                    return True
                else:
                    return evaluate_last_element(current_node.next)

    def remove_if(self, functor):
        pass

    def empty(self):
        return self._head is None

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    linked_list.push_front(0)
    linked_list.insert(2, 5)
    print(linked_list)
    print(linked_list.pop_back())
    print(linked_list)
    print(linked_list.pop_front())
    print(linked_list)
    print(linked_list.empty())
    print(linked_list.insert(6, 10))
    linked_list.push_back(6)
    linked_list.push_back(7)
    linked_list.push_back(8)
    print(linked_list)
    print(linked_list.remove(8))
    print(linked_list)
    print(linked_list.remove(5))
    print(linked_list)
    print(linked_list.remove(6))
    print(linked_list)
    print(linked_list.remove(1))
    print(linked_list)
