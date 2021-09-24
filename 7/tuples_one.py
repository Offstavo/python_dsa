# How to create a new tuple

newTuple = 'a','b','c','d','e'
print(newTuple)

newTuple = ('a','b','c','d','e')
print(newTuple)

newTuple1 = ('a',)
# single element tuples should be declared with a comma or will be treated as a string value
print(newTuple1)

newTuple1 = tuple('abcde')
print(newTuple1)