#insertion into two dimensional array
#Time complexity O(m,n)
# m is the number of colums and n number of elements

import numpy as np

twoDArray = np.array([[11, 15, 10, 6],[10, 14, 11, 5],[12, 17, 12, 8],[15, 18, 14, 9]])

#add new column
# newTwoDArray = np.insert(twoDArray, 0, [[1,2,3,4]], axis=1)
# print(newTwoDArray)

#add new row 
newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)
