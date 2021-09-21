# Searching for an element in a list

myList = [10,20,30,40,50,60,70,80,90]

# Using in operator

if 20 in myList:
    print(myList.index(20))
else:
    print("Element not in list")

# Using linear search
def searchInList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist'

print(searchInList(myList,100))
