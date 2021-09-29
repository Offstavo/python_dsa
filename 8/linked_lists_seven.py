# Create circular singlylinked list

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None

class CircularSinglyLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None

    def __iter__ (self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # Creation of circular singly linked list
    def createCSSL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

circularSLL = CircularSinglyLinkedList()
circularSLL.createCSSL(1)

print([node.value for node in circularSLL])

# Code worked as expected