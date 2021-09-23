# Traverse elements in a dictionary

myDict = {'name':'Edy','age':26,'address':'London'}

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)