# Deletion of an entire linked list

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    def insertSSL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def deleteEntireSSL(self):
        if self.head is None:
            print("The SSL does not exist")
        else:
            self.head = None
            self.tail = None

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSSL(1,1)
singlyLinkedList.insertSSL(2,1)
singlyLinkedList.insertSSL(3,1)
singlyLinkedList.insertSSL(4,1)
singlyLinkedList.insertSSL(0,0)
singlyLinkedList.insertSSL(0,4)

print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteEntireSSL()
print([node.value for node in singlyLinkedList])

# Code worked as expected