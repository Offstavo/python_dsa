# Searching for an element in twodimensional array
import numpy as np

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])

# This fuction uses a linear search
def searchTDArray(array, value): # O(m,n)
    for i in range(len(array)): # O(n)
        for j in range(len(array[0])): # O(1)
            if array[i][j] == value:
                return 'The value is located at index' +str(i)+" "+str[j]

        return 'The element is fourd'

        # Time complexity O(mn)
        # Space complexity O(1)

print(searchTDArray(twoDArray, 14))
