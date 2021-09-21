# Access array element

# myArray[0] = "a"
# myArray[3] = "d"

from array import *

arr1 = array('i',[1,2,3,4,5])

def accessElement(array,index):
    if index > len(array): #O(1)
        print('There is not any element in this index') #O(1)
    else:
        print(array[index]) #O(1)

accessElement(arr1, 1)
accessElement(arr1, 8)

#time complexity O(1)
#space complexity O(1)