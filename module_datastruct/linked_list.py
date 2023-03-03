class Node:

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_beginning(self, data):
        """Добавляет элемент в начало списка."""
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        """Добавляет элемент в конец списка."""
        new_node = Node(data, None)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        """Выводит в консоль данные из односвязного списка"""
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)
        return ll_string


ll = LinkedList()
ll.insert_beginning({'id': 1})
ll.insert_at_end({'id': 2})
ll.insert_at_end({'id': 3})
ll.insert_beginning({'id': 0})
ll.print_ll()
