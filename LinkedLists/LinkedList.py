class LinkedList:
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def insertNodeAtStart(self, value):
        #print "Insert Node at the begning"
        head = LinkedList(value)
        head.nextNode = self
        return head;

    def insertNodeAtEnd(self):
        print "Insert Node at the end"
    def printLinkedList(self, list):
        print "Printing the Linked List"
        while list.nextNode != None:
            print list.value
            list = list.nextNode

def main():
    print "Inside main"
    list = LinkedList()
    for i in range(0, 10, 1):
        list = list.insertNodeAtStart(i)
    list.printLinkedList(list)

main()