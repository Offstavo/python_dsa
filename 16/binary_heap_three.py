# size of binary heap

class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

# Space complexity O(n)

def sizeOfHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

newBinaryHeap = Heap(5)
print(sizeOfHeap(newBinaryHeap))

# code worked as expected