# Insert/Update a list

myList = [1,2,3,4,5,6,7]
print(myList)

# Update
myList[2] =33
print(myList)
myList[4] = 55
print(myList)

# Insert

# Using insert() method
myList.insert(5,35)
print(myList)

# Using append() method
myList.append(11)
print(myList)

# Using extend() method
newList = [11,12,13,14]
myList.extend(newList)
print(myList)