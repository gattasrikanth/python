#  Copyright (c) 2019.
#  Feel free to reuse this code as you like.
#  This code is for educational purpose only.

class SinglyLinkedList:
    def __init__(self):
        self.nextNode = Node()

    def insertNodeAtStart(self, value=None):
        """
        Insert a node at the starting of the linked list.
        :param value: Value to be inserted into the list.
        """
        node = Node(value)
        node.nextNode = self.nextNode;
        self.nextNode = node

    def insertNodeAtEnd(self, value=None):
        """
        Insert a node at the end of the linked list.
        :param value: Value to be inserted into the list.
        """
        node = Node(value)
        if self.nextNode.value is None:
            self.nextNode = node
            return
        currentNode = self.nextNode
        while currentNode.nextNode is not None:
            currentNode = currentNode.nextNode
        currentNode.nextNode = node

    def printLinkedList(self):
        print "\n Printing the Linked List"
        node = self.nextNode
        while node:
            print node.value,
            node = node.nextNode


class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextNode = None


def main():
    print "Inside main"
    frontlist = SinglyLinkedList()
    backlist = SinglyLinkedList()
    for i in range(0, 10, 1):
        print "adding " , i , " now"
        frontlist.insertNodeAtStart(i)
        backlist.insertNodeAtEnd(i)
    frontlist.printLinkedList()
    backlist.printLinkedList()


main()
