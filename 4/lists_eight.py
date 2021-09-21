myList = [2,4,3,1,5,7]

myList = myList.sort()
print(myList)

myList = [2,4,3,1,5,7]
myList.append(10)
# myList.append([10]) wrong way to add element here another array is being added
# myList = myList + [10] you can also add elements using contatenate
print(myList)

myList = [2,4,3,1,5,7]
myList.sort()
print(myList)
# When the list is sorted it prints the sorted list

#a copy of the original can be made to avoid this
myList = [2,4,3,1,5,7]
orig = myList[:]
myList.sort()
print(orig)
print(myList)

# Alternative
# Using the sorted funtion the original value is not touched
myList = [2,4,3,1,5,7]
sorted(myList)
print(myList)