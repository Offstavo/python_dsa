# Traversal using pre order

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)  # O(n/2)
    preOrderTraversal(rootNode.rightChild) # O(n/2)

preOrderTraversal(newBT)

# Time complexity O(n)
# Space complexity O(n)
# Code worked as expected