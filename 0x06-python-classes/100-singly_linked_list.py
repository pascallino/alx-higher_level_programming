#!/usr/bin/python3
"""

This module contains a class that defines a square and its size and its
position on the screen, checking if the given values are right, and a setter
and getter methods to set or get them. There's also an area method that returns
the area of the square, another one that handles the print of the square.

"""


class Node():
    """Defines a node."""

    def __init__(self, data, next_node=None):
        """Sets the necessary attributes for the Node object.

        Args:
            data (int): the size of the Node
            next_node: the node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get or set the position of the square."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList():
    """ define a new single list class """
    def __init__(self):
        self.__head = None

    def __str__(self):
        """Sets the print behavior of the SinglyLinkedList object."""
        sll_str = ""
        node = self.__head

        if node is not None:
            while node is not None:
                sll_str += str(node.data) + '\n'
                node = node.next_node

        return sll_str[:-1]

    def sorted_insert(self, value):
        node = self.__head

        if node is None or self.__head.data >= value:
            self.__head = Node(value, self.__head)
        else:
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            node.next_node = Node(value, node.next_node)
