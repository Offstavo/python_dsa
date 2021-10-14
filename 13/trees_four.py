# Traversal using in orderTraversal

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

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild) # O(n/2)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild) # O(n/2)

inOrderTraversal(newBT)

# Time complexity O(n)
# Space complexity O(n)

# code worked as expected