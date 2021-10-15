# Delete entire tree

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

    def deleteBT(self):
        self.customList = None
        return "The BT has been successfully deleted"

newBt = BinaryTree(8)
newBt.insertNode("Drinks")
newBt.insertNode("Hot")
newBt.insertNode("Cold")
newBt.insertNode("Tea")
newBt.insertNode("Coffee")

# print(newBt.deleteNode("Tea"))
print(newBt.deleteBT())

newBt.levelOrderTraversal(1) 
# generated error because tree has been deleted

# Code worked as expected
# Space complexity O(n)