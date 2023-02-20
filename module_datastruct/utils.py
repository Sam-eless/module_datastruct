class Node:

    def __init__(self, data, top=None):
        self.data = data
        self.top = top


class Stack:
    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        new_node = Node(data, None)
        new_node.top = self.top
        self.top = new_node


n1 = Node(5, None)
n2 = Node('a', n1)
print(n1.data)
print(n2.data)
print(n1)
stack = Stack(n2)
stack.push('data3')
print(stack.top)
