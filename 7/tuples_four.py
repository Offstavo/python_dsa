# Search for elements in a tuple

newTuple = ('a','b','c','d','e')

# Using in operator
print('b' in newTuple)

# Using linear search
def searchTuple(pTuple, element):
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
        else:
            return "Element not in tuple"

print(searchTuple(newTuple, 'b'))