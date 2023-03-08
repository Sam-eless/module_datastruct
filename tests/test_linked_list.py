import unittest
from module_datastruct.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1})
        ll.insert_beginning({'id': 0})
        self.assertEqual(ll.head.data, {'id': 0})
        self.assertEqual(ll.head.next_node.data, {'id': 1})

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_end({'id': 2})
        ll.insert_at_end({'id': 3})
        self.assertEqual(ll.tail.data, {'id': 3})
        self.assertEqual(ll.tail.next_node, None)

    def test_print_ll(self):
        ll = LinkedList()
        self.assertEqual(str(ll.print_ll()), f' {None}')
        ll.insert_beginning("Первый")
        ll.insert_beginning("Нулевой")
        ll.insert_at_end("Второй")
        ll.insert_at_end("Третий")
        self.assertEqual(str(ll.print_ll()), " Нулевой -> Первый -> Второй -> Третий -> None")

    def test_to_list(self):
        ll = LinkedList()
        self.assertEqual(ll.to_list(), None)
        ll.insert_beginning({'id': 1, 'one': 'first'})
        ll.insert_at_end({'id': 2, 'two': 'second'})
        self.assertEqual(ll.to_list(), [{'id': 1, 'one': 'first'}, {'id': 2, 'two': 'second'}])

    def test_get_data_by_id(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'one': 'first'})
        ll.insert_at_end('idusername')
        ll.insert_at_end([1, 2, 3])
        ll.insert_at_end({'id': 2, 'two': 'second'})
        self.assertEqual(ll.get_data_by_id(2), {'id': 2, 'two': 'second'})
