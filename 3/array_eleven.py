# Traversing twoDArray
import numpy as np

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])

def traverseTDArray(array):
    for i in range(len(array)): # O(mn) if m == to n then time is O(n^2)
        for j in range(len(array[0])): # O(n)
            print(array[i][j]) # O(1)
# Space complexity O(1)

traverseTDArray(twoDArray)