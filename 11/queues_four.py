# collections.deque to make a queue
# collections module to create fifo queue

from collections import deque

customQueue = deque(maxlen = 3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)
# customQueue.popleft()
customQueue.clear()
print(customQueue)

# code worked as expected