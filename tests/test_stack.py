"""Здесь надо написать тесты с использованием unittest для модуля stack."""
# from src.stack import Node, Stack
#
#
# def test_Node():
#     n1 = Node(5, None)
#     n2 = Node('a', n1)
#     assert n1.data == 5
#     assert n2.data == 'a'
#     assert n2.next_node.data == 5
#     assert n2.next_node.next_node == None
#     assert n2.next_node.next_node == None
#
#
# def test_Stack():
#     stack = Stack()
#     stack.push('data1')
#     stack.push('data2')
#     stack.push('data3')
#     assert stack.top.data == 'data3'
#     assert stack.top.next_node.data == 'data2'
#     assert stack.top.next_node.next_node.data == 'data1'
#     assert stack.top.next_node.next_node.next_node == None
#     stack.pop()
#     assert stack.top.data == 'data2'
#     stack.pop()
#     assert stack.top.data == 'data1'
#     stack.pop()
#     assert stack.top == None
#     stack.pop()
#     assert stack.top == None


import unittest

from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    def test_Node(self):
        n1 = Node(5, None)
        n2 = Node('a', n1)
        self.assertEquals(n1.data, 5)
        self.assertEquals(n2.data, 'a')
        self.assertEquals(n2.next_node.data, 5)
        self.assertEquals(n2.next_node.next_node, None)


class TestStack(unittest.TestCase):
    def test_Stack(self):
        stack = Stack()
        stack.push('data1')
        stack.push('data2')
        stack.push('data3')
        self.assertEquals(stack.top.data, 'data3')
        self.assertEquals(stack.top.next_node.data, 'data2')
        self.assertEquals(stack.top.next_node.next_node.data, 'data1')
        self.assertEquals(stack.top.next_node.next_node.next_node, None)
        stack.pop()
        self.assertEquals(stack.top.data, 'data2')
        stack.pop()
        self.assertEquals(stack.top.data, 'data1')
        stack.pop()
        self.assertEquals(stack.top, None)
        stack.pop()
        self.assertEquals(stack.top, None)


if __name__ == '__main__':
    unittest.main()
