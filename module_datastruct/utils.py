class Node:

    def __init__(self, data, prev):
        self.data = data
        self.prev = prev


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.prev = self.top
        self.top = new_node



n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
