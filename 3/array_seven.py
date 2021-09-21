# Operetions on one dimensional arrays

# 1. Create an array and traverse
from array import *

my_array = array('i',[1,2,3,4,5])

for i in my_array:
    print(i)

# 2. Access individual elements through indexes
print("Step 1")
print(my_array[3])

# 3. Append any value to the array using append() method
print("Step 2")
my_array.append(6)
print(my_array)
#append() inserts value at the end of the array

# 4. Insert value into array using insert() method
print("Step 4")
my_array.insert(3,11)
print(my_array)

# 5. Extend python array using extend() method
print("Step 5")
my_array1 = array('i',[10,11,12])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list using fromlist() method
print("Step 6")
tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)

# 7. Remove any element using remove() method
print("Step 7")
my_array.remove(11)
print(my_array)

# 8. Remove last array elemnt using pop() method
print("Step 8")
my_array.pop()
print(my_array)

# 9. Fetch index of any element using index() method
print("Step 9")
print(my_array.index(21)) 

# 10. Reverse python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer information using buffer_info() method
print("Step 11")
print(my_array.buffer_info())

# 12. Check number of occurences of an element using count() method
print("Step 12")
my_array.append(11)
print(my_array.count(11))
print(my_array)

# 13. Convert any array tostring using tostring() method
# print("Step 13")
# strTemp = my_array.tostring()
# print(strTemp)
# ints = array('i')
# ints.fromstring(strTemp)
# print(ints)

# 14. Convert array to list
print("Step 14")
print(my_array.tolist())

# 15. Append a string to char using fromstring() method
# Check step 13

# 16. Slice Elements of an array
print("Step 16")
print(my_array[1:4])
print(my_array[2:])
print(my_array[:4])
print(my_array[:])