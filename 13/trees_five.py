# Traversal using postOrder

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild) # O(n/2)
    postOrderTraversal(rootNode.rightChild) # O(n/2)
    print(rootNode.data)

postOrderTraversal(newBT)

# code worked as expected

# Time complexity O(n)
# Space complexity O(n)