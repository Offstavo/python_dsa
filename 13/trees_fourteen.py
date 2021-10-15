# Search a value in a binry tree using level order traversal

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

    def searchNode(self, nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not found"

newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
print(newBT.insertNode("Hot"))
print(newBT.insertNode("Cold"))
# print(newBT.searchNode("Tea"))
print(newBT.searchNode("Hot"))