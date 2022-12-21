#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

"""A class that defines single linked list"""


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current_node = self.head
        while current_node is not None:
            print("{}".format(str(current_node.data)), end="\n")
            current_node = current_node.next_node

        return ""

    def sorted_insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            current_node = self.head
            while current_node:
                temp = current_node.data
                if temp > value:
                    current_node.data = value
                    node.data = temp

                if current_node.next_node is None:
                    current_node.next_node = node
                    break

                current_node = current_node.next_node
