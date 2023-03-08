class Node:

    def __init__(self, data, top=None):
        self.data = data
        self.top = top


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        """Добавляет в стек элемент в виде узла."""
        new_node = Node(data, None)
        new_node.top = self.top
        self.top = new_node

    def pop(self):
        """Удаляет из стека верхний элемент (последний добавленный)."""
        remove = self.top
        self.top = self.top.top
        return remove.data
