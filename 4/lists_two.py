# Traversing and accessing the elements of a list
shoppingList = ['Milk','Cheese','Butter']

# Accesing
print(shoppingList[1])
# print(shoppingList[4])
# Ouputs an error because list doesnt have an index of 4

# In operator
print('Milk' in shoppingList)
print('Bread' in shoppingList)

print(shoppingList[-1])
# print(shoppingList[-4])
# Outputs an error because list doesnt have and index of -4

# Traversing
for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])

# Traversing empty list
empty = []
for i in empty:
    print(i)
