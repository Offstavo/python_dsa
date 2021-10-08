# Deletion of a node from singly linked list

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

    def deleteNode(self, location):
        if self.head is None:
            print("The SSL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head == None
                    self.tail == None
                else:
                    self.head == self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head == None
                    self.tail == None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSSL(1,1)
singlyLinkedList.insertSSL(2,1)
singlyLinkedList.insertSSL(3,1)
singlyLinkedList.insertSSL(4,1)
singlyLinkedList.insertSSL(0,0)
singlyLinkedList.insertSSL(0,4)

print([node.value for node in singlyLinkedList])
singlyLinkedList.deleteNode(3)
print([node.value for node in singlyLinkedList])

# code works but when it comes to deleteNode(0) it doesnt work