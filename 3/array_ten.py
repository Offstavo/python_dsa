# Access elements of a two dimensional array
# a[i][j] i is the row and j is the column

import numpy as np

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]): #O(1)
        print('Incorrect index') # O(1)
    else:
        array[rowIndex][colIndex] #O(1)
    # Time complexity O(1)
    # Space complexity O(1)
    accessElements(twoDArray, 2, 3)