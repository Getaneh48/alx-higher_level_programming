#!/usr/bin/python3

""" a class represents a single linked list Node """


class Node:
    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data of the Node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """sets the data of the Node"""
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """get the data of the Node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """A class that defines single linked list"""

    def __init__(self):
        """Initialize the instance"""
        self.head = None

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        current_node = self.head
        while current_node is not None:
            print("{}".format(str(current_node.data)), end="\n")
            current_node = current_node.next_node

        return ""

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
           The node is inserted into the list at the correct
           ordered numerical position.
           Args:
               value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.head is None:
            new.next_node = None
            self.head = new
        elif self.head.data > value:
            new.next_node = self.head
            self.head = new
        else:
            tmp = self.head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
