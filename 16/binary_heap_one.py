# creation of binary heap

class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

# Space complexity of creation O(n)

newBinaryHeap = Heap(5)

# code worked as expected