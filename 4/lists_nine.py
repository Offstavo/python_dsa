# Arrays vs Lists 
# Similarities

# Diffrences
# 1. Arrays are good for arithmetic computations
import numpy as np

myArray = np.Array([1,2,3,4,5,6])
myList = [1,2,3,4,5]

print(myArray/2)
# print(myList/2) this operation returns an error

# 2. Lists can have diffrent datatypes

myArray = np.Array([1,2,3,4,5,6,'a'])
myList = [1,2,3,4,5,'a']
print(myArray)
print(myList)

