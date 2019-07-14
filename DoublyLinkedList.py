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

    def __len__(self):
        current_node = self._head
        size = 0
        while current_node is not None:
            size += 1
            current_node = current_node.next
        return size

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

    def insert(self, pos, node) -> bool:
        if self.empty():
            return False
        else:
            current_node = self._head
            while current_node.next is not None and current_node.data != pos:
                current_node = current_node.next
            if current_node.next is None and current_node.data == pos:
                new_node = Node(node)
                current_node.next = new_node
                new_node.prev = current_node
                return True
            elif current_node.next is not None:
                new_node = Node(node)
                current_node.next.prev = new_node
                new_node.next = current_node.next
                new_node.prev = current_node
                current_node.next = new_node
                return True
            else:
                return False

    def remove(self, node) -> bool:
        if self.empty():
            return False
        else:
            current_node = self._head
            while current_node.next is not None and current_node.data != node:
                current_node = current_node.next
            if current_node.next is None and current_node.data == node:
                current_node.prev.next = None
                return True
            elif current_node.next is not None:
                if current_node.prev is None:
                    self._head = current_node.next
                    current_node.next.prev = None
                    return True
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    return True
            else:
                return False

    def remove_if(self, functor):
        if self.empty():
            return
        else:
            current_node = self._head
            while current_node is not None:
                if functor(current_node.data):
                    new_current = current_node.next
                    if current_node.prev is None:
                        self._head = new_current
                        new_current.prev = None
                    elif current_node.next is None:
                        current_node.prev.next = new_current
                    else:
                        current_node.prev.next = current_node.next
                        current_node.next.prev = current_node.prev
                    current_node.next = None
                    current_node.prev = None
                    current_node = new_current
                else:
                    current_node = current_node.next

    def __iter__(self):
        return DoublyLinkedListIterator(self._head)


class DoublyLinkedListIterator():
    def __init__(self, head):
        self._current = head

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            current_node = self._current
            self._current = self._current.next
            return current_node

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
    double_list.insert(-10, -9)
    print(double_list)
    double_list.insert(0, 1)
    print(double_list)
    double_list.insert(2, 3)
    print(double_list)
    double_list.remove(0)
    print(double_list)
    double_list.remove(-1)
    print(double_list)
    double_list.remove(1)
    print(double_list)
    double_list.push_front(-20)
    double_list.push_back(0)
    double_list.push_back(1)
    double_list.push_back(-15)
    double_list.insert(0, -2)
    print(double_list)
    double_list.remove_if(lambda x: x < 0)
    print(double_list)
    print(len(double_list))

    for node in double_list:
        print(node)
