# Search for an element in a singly linked list

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
                nextNode.next = nextNode

    def searchSSL(self, nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value of the node does not exist in the list"

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSSL(1,1)
singlyLinkedList.insertSSL(2,1)
singlyLinkedList.insertSSL(3,1)
singlyLinkedList.insertSSL(4,1)

singlyLinkedList.insertSSL(0,0)
singlyLinkedList.insertSSL(0,3)
print([node.value for node in singlyLinkedList])
print(singlyLinkedList.searchSSL(3))

# Code dint work as expected