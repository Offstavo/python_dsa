# find peek of binary heap

class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

# Space complexity of creation method O(n)

def peekOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

newBinaryHeap = Heap(5)

# code worked as expected