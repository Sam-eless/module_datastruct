class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Добавить элемент в конец очереди."""
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def dequeue(self):
        """Удалить элемент из начала очереди."""
        if self.head is not None:
            remove = self.head
            self.head = self.head.next_node
            return remove.data
        else:
            return None
