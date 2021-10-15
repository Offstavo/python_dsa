# Creation of a binary tree using python lists

class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

newBT = BinaryTree(8)

# skeleton code to be used in other modules
# space complexity O(n)

# code worked as expected