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


# Homework_1
# n1 = Node(5, None)
# n2 = Node('a', n1)
# print(n1.data)
# print(n2.data)
# print(n1)
# stack = Stack(n2)
# stack.push('data3')
# print(stack.top)

# Homework_2
stack = Stack()
stack.push('data1')
data = stack.pop()
print(stack.top)
print(data)

stack = Stack()
stack.push('data1')
stack.push('data2')
data = stack.pop()

print(stack.top.data)

print(data)
