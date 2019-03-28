#  Copyright (c) 2019.
#  Feel free to reuse this code as you like.
#  This code is for educational purpose only.

class SinglyLinkedList:
    def __init__(self):
        self.value = None

    def insertNodeAtStart(self, value=None):
        """
        Insert a node at the starting of the linked list.
        :param value: Value to be inserted into the list.
        :return: returns the new HEAD.
        """
        node = Node(value)
        node.nextNode = self.value;
        self.value = node

    def insertNodeAtEnd(self):
        print "Insert Node at the end"

    def printLinkedList(self):
        print "Printing the Linked List"
        node = self.value
        while node.nextNode is not None:
            print node.value
            node = node.nextNode


class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextNode = None


def main():
    print "Inside main"
    list = SinglyLinkedList()
    for i in range(10, 1, -1):
        list.insertNodeAtStart(i)
    list.printLinkedList()
    #print list.insertNodeAtStart.__doc__


main()
