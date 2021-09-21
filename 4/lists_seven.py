# Strings and lists

# Convert strings to list
a = 'spam'
b = list(a)
print(b)

a = 'spam spam spam'
a = a.split()
print(a)

a = 'spam-spam1-spam'
delimiter = '-'
a = a.split()
print(a)

# Convert lists to strings
a = 'spam-spam1-spam'
delimiter = '-'
b = a.split(delimiter)
print(delimiter.join(b))