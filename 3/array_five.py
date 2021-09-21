#Finding an element in an array
from array import *

arr1 = array('i',[1,2,3,4,5])

def searchInArray(array, value):
    for i in array: #O(n)
        if i == value: #O(1)
            return array.index(value) #O(1)
    return "The element does not exist in this array" #O(1)

    #Time comlexity O(n)
    #Space complexity O(1)

print(searchInArray(arr1, 6))