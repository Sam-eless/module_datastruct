import unittest

from module_datastruct.utils import Node, Stack
from module_datastruct.custom_queue import Queue

node1 = Node("data1")
node2 = Node('data2', node1)
node2.top = node1
stack = Stack(node2)
stack.push("data3")
stack.push("data4")
stack.push("data5")


class TestUtils(unittest.TestCase):

    def test_utils(self):
        self.assertEqual(node1.top, None)
        self.assertEqual(node1.data, "data1")
        self.assertEqual(stack.top.data, "data5")
        self.assertEqual(stack.top.top.top.top, node2)
        self.assertEqual(stack.top.top.top.top.top.data, "data1")

    def test_stack_pop(self):
        stack.push("data6")
        self.assertEqual(stack.pop(), 'data6')
        self.assertEqual(stack.top.data, 'data5')

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue("data1")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.tail.data, "data1")
        queue.enqueue("data2")
        self.assertEqual(queue.head.data, "data1")
        self.assertEqual(queue.head.next_node.data, "data2")

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue("data1")
        queue.enqueue("data2")
        self.assertEqual(queue.dequeue(), "data1")
        self.assertEqual(queue.dequeue(), "data2")
        self.assertEqual(queue.dequeue(), None)


