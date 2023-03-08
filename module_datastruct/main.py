from module_datastruct.custom_queue import Queue
from module_datastruct.linked_list import LinkedList
from module_datastruct.stack import Stack


def main():
    # # Homework_1
    # # ________________________
    # n1 = Node(5, None)
    # n2 = Node('a', n1)
    # print(n1.data)
    # print(n2.data)
    # print(n1)
    # stack = Stack(n2)
    # stack.push('data3')
    # print(stack.top)

    # # Homework_2
    # # ________________________
    # stack = Stack()
    # stack.push('data1')
    # data = stack.pop()
    # print(stack.top)
    # print(data)
    #
    # stack = Stack()
    # stack.push('data1')
    # stack.push('data2')
    # data = stack.pop()
    #
    # print(stack.top.data)
    # print(data)

    # # Homework 3
    # # ________________________
    # queue = Queue()
    # queue.enqueue('data1')
    # queue.enqueue('data2')
    # queue.enqueue('data3')
    #
    # print(queue.head.data)
    # print(queue.head.next_node.data)
    # print(queue.tail.data)
    # print(queue.tail.next_node)
    # print(queue.tail.next_node.data)

    # # Homework 4
    # # ________________________
    # queue = Queue()
    # queue.enqueue('data1')
    # queue.enqueue('data2')
    # queue.enqueue('data3')
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())

    # Homework_5
    # ________________________
    # ll = LinkedList()
    # ll.insert_beginning({'id': 1})
    # ll.insert_at_end({'id': 2})
    # ll.insert_at_end({'id': 3})
    # ll.insert_beginning({'id': 0})
    # ll.print_ll()

    # Homework_6
    # ________________________
    ll = LinkedList()
    ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
    ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
    ll.insert_beginning({'id': 0, 'username': 'serebro'})

    # метод to_list()
    lst = ll.to_list()
    for item in lst:
        print(item)

    # get_data_by_id()
    user_data = ll.get_data_by_id(3)
    print(f'\n{user_data}\n')

    # работа блока try/except
    ll_2 = LinkedList()
    ll_2.insert_beginning({'id': 1, 'username': 'lazzy508509'})
    ll_2.insert_at_end('idusername')
    ll_2.insert_at_end([1, 2, 3])
    ll_2.insert_at_end({'id': 2, 'username': 'mosh_s'})
    user_data = ll_2.get_data_by_id(2)
    print(user_data)


if __name__ == '__main__':
    main()
