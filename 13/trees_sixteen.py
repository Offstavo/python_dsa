# In order traversal

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)    # O(n/2)
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)     # O(n/2)

newBt = BinaryTree(8)
newBt.insertNode("Drinks")
newBt.insertNode("Hot")
newBt.insertNode("Cold")
newBt.insertNode("Tea")
newBt.insertNode("Coffee")

newBt.inOrderTraversal(1)

# Code worked as expected
# Space complexity O(n)