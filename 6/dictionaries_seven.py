# Dictionary operations built in functions

myDict = {'one':'uno', 'two':'dos', 'three':'tres', 'four':'cuarto'}

print('one' in myDict)
print('uno' in myDict) # uno only prints the keys
print('uno' in myDict.values())
# TIme complexity for in operator is O(1)

for key in myDict:
    print(key)

for key in myDict:
    print(myDict[key])

for key in myDict:
    print(key, myDict[key])

# myDict = {1: True, 2: True}
# print(all(myDict))

# myDict = {0: False, 1: True}
# print(all(myDict))

# myDict = {0: True, 1: False, 2: True}
# print(all(myDict))

# newDict = {}
# print(all(newDict))
# print(any(newDict))
# print(any(myDict))

print(len(myDict))

# myDict = {'e':1, 'a':2, 'u':3, 'o':4, 'i':5}
# print(sorted(myDict))
# print(sorted(myDict, reverse = True))

# myDict = {'ea':1, 'aas':2, 'udd':3, 'sseo':4, 'werwi':5}
# print(sorted(myDict, key=len))
# sorted based on length