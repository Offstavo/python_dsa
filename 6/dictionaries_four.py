# Search for an element in a dictionary

myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
        else:
            return 'Value does not exist'

print(searchDict(myDict, 26))