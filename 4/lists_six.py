# List operations / functions

# Concatenation
a = [1,2,3]
b = [4,5,6,7]
c = a + b
print(c)

# * Operator
a = [0,1]
a = a * 4
print(a)

# get length using len() method
a = [1,2,3,4,6]
print(len(a))

# get maximum using max() method
a = [1,2,3,4,6]
print(max(a))

# get minimum using min() method
a = [1,2,3,4,6]
print(min(a))

# get sum using sum() method
a = [1,2,3,4,6]
print(sum(a))

# calculate average by combining method
a = [1,2,3,4,6]
print(sum(a)/len(a))

# Exercise code conversion to get input of numbers from the user and output average
myList = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    myList.append(value)
average = sum(myList) / len(myList)

print(average)



