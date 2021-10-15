# Delete a node from python tree

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

    def levelOrderTraversal(self, index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"

newBt = BinaryTree(8)
newBt.insertNode("Drinks")
newBt.insertNode("Hot")
newBt.insertNode("Cold")
newBt.insertNode("Tea")
newBt.insertNode("Coffee")

# print(newBt.deleteNode("Tea"))
print(newBt.deleteNode("Hot"))

newBt.levelOrderTraversal(1)

# Code worked as expected
# Space complexity O(n)