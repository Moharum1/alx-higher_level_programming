#!/usr/bin/python3
"""A node class"""

class Node:
    """
        Args:
            data : data in the node of type Int
            next_node : a reference to the next Node
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node  = next_node

    """getter for the propert data"""
    @property
    def data(self):
        return self.__data
    
    """Setter for the propert data"""
    @data.setter
    def data(self, value):
        if not isinstance(value,int):
            raise TypeError("data must be an integer")

    """getter for the property next_node"""  
    @property
    def next_node(self):
        return self.__next_node
    
    """Setter for the property next_node"""
    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")

"""A single linked list"""       
class SinglyLinkedList:
    """
        Args :
            None 
    """
    def __init__(self):
        self.__head = None

    def __str__(self) -> str:
        print_node = []
        current_node = self.__head
        while current_node is not None:
            print_node.append(str(current_node.data))
            current_node = current_node.next_node

        return "\n".join(print_node)

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)