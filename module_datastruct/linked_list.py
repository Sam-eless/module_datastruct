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

    def to_list(self):
        """ Возвращает список с данными, содержащимися в односвязном списке LinkedList."""
        ll_list = []
        node = self.head
        if node is None:
            return None
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    def get_data_by_id(self, item_id):
        """ Возвращает первый найденный в LinkedList словарь с ключом id,
        значение которого равно переданному в метод значению."""
        item_list = self.to_list()
        for item in item_list:
            try:
                if item["id"] == item_id:
                    return item
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
