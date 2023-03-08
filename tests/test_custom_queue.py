import unittest
from module_datastruct.custom_queue import Queue

queue = Queue()


class TestCustomQueue(unittest.TestCase):

    def test_enqueue(self):
        queue.enqueue("data1")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.tail.data, "data1")
        queue.enqueue("data2")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next_node.data, "data2")

    def test_dequeue(self):
        queue.enqueue("data1")
        queue.enqueue("data2")
        self.assertEqual(queue.dequeue(), "data1")
        self.assertEqual(queue.dequeue(), "data2")
        self.assertEqual(queue.dequeue(), None)
